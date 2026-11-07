Title:

Content selection saved. Describe the issue below:

Description:

![](https://arxiv.org/static/base/1.0.1/images/icons/smileybones-small.svg)arXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) ×

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2605.23054v1 \[cs.CL\] 21 May 2026

# Model Collapse as Cultural Evolution

Dongxin Guo [ORCID 0009-0000-2388-1072](https://orcid.org/0009-0000-2388-1072 "ORCID 0009-0000-2388-1072")Affiliation: The University of Hong Kong
Affiliation: Hong Kong, China
Email: [bettyguo@connect.hku.hk](mailto:)Jikun Wu [ORCID 0000-0002-2327-4157](https://orcid.org/0000-0002-2327-4157 "ORCID 0000-0002-2327-4157")Affiliation: Stellaris AI Limited
Affiliation: Hong Kong, China
Email: [hk950014@connect.hku.hk](mailto:)Siu Ming Yiu [ORCID 0000-0002-3975-8500](https://orcid.org/0000-0002-3975-8500 "ORCID 0000-0002-3975-8500")Affiliation: The University of Hong Kong
Affiliation: Hong Kong, China
Email: [smyiu@cs.hku.hk](mailto:)

###### Abstract

Model collapse, the progressive degradation of LLMs trained on their own outputs, has been characterized statistically but lacks a _linguistic_ explanation for which structures degrade, in what order, and why. We show that iterated learning theory from cultural evolution fills this gap. We derive five falsifiable predictions, distinguish those uniquely discriminative for the theory from confirmatory ones, and test them by self-training LLaMA-2-7B and Mistral-7B over 10 generations in English, German, and Turkish. The critical discriminative finding: compositionality follows a _non-monotonic_ trajectory (initially rising, then falling) under unfiltered self-training. This signature persists with maximally regular seed data (ruling out noise removal) and is sustained only by task-grounded filtering, not random filtering, providing the first LLM-scale evidence for the compression–communication tradeoff. All predictions are confirmed with large effect sizes (Hedges’ g>1.6g>1.6; BF10>100\\text{BF}\_{10}>100), and LLM regularization gradients closely match human behavioral data (R2=0.94R^{2}=0.94). These results reframe model collapse as a cultural transmission phenomenon and yield concrete principles for self-training pipeline design.

## 1 Introduction

Why are human languages structured the way they are? Cultural evolution theory offers a compelling answer: languages are shaped by the process of being learned and transmitted ( [Christiansen and Chater, 2016](https://arxiv.org/html/2605.23054v1#bib.bib35 ""); [Christiansen and Chater, 2015](https://arxiv.org/html/2605.23054v1#bib.bib36 "")). When language passes through chains of learners, each generation’s inductive biases are amplified, progressively eliminating unpredictable variation and promoting learnable structure ( [Kirby et al., 2008](https://arxiv.org/html/2605.23054v1#bib.bib61 ""); [Kirby et al., 2014](https://arxiv.org/html/2605.23054v1#bib.bib33 "")). This process, formalized as _iterated learning_( [Griffiths and Kalish, 2007](https://arxiv.org/html/2605.23054v1#bib.bib31 "")), provides a mathematical explanation for core properties of language: regularity, compositionality, and Zipfian frequency distributions emerge from the dynamics of cultural transmission itself. Critically, [Kirby et al. (2015)](https://arxiv.org/html/2605.23054v1#bib.bib34 "") demonstrated that compositionality requires both compression pressure (from the learning bottleneck) and communication pressure (from the need to be expressive); compression alone produces degenerate languages.

In a seemingly related development, training LLMs on their own outputs causes _model collapse_: distributional tails disappear, diversity decreases, and outputs converge toward degenerate forms ( [Shumailov et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib68 ""); [Alemohammad et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib3 "")). This phenomenon has been characterized through statistical estimation theory ( [Dohmatob et al., 2024b](https://arxiv.org/html/2605.23054v1#bib.bib4 ""); [Dohmatob et al., 2024a](https://arxiv.org/html/2605.23054v1#bib.bib5 ""); [Dohmatob et al., 2025](https://arxiv.org/html/2605.23054v1#bib.bib6 "")), with [Guo et al. (2024)](https://arxiv.org/html/2605.23054v1#bib.bib66 "") documenting linguistic diversity decline across several dimensions and [Seddik et al. (2024)](https://arxiv.org/html/2605.23054v1#bib.bib41 "") providing information-theoretic analysis. While these accounts accurately describe the statistical mechanics of collapse, they provide limited insight into _which_ linguistic properties are affected, in what order, and why.

The conceptual connection between model collapse and cultural evolution has been established by several recent contributions. [Ren et al. (2024)](https://arxiv.org/html/2605.23054v1#bib.bib42 "") formally showed that LLM self-evolution instantiates Bayesian iterated learning and proved monotonic bias amplification across generations. [Shumailov et al. (2024)](https://arxiv.org/html/2605.23054v1#bib.bib68 "") argued in a _Nature_ correspondence that the compression–expressivity tradeoff from human language transmission explains why self-training degrades. [Kouwenhoven et al. (2025b)](https://arxiv.org/html/2605.23054v1#bib.bib69 "") tested iterated learning with LLMs in referential games, finding that LLMs produce degenerate vocabularies without sufficient compression pressure, while [Galke et al. (2023)](https://arxiv.org/html/2605.23054v1#bib.bib71 "") reviewed language evolution insights for LLMs broadly. We build on these foundations by providing the first systematic test of _discriminative_ predictions (those that distinguish iterated learning from generic model collapse) at full LLM scale on natural language.

We derive five predictions from cultural evolution theory and explicitly distinguish their discriminative status:

#### P1: Frequency-dependent loss order ( _partially discriminative_).

Low-frequency variants should be lost before high-frequency ones, following a specific log-linear gradient matching human regularization ( [Reali and Griffiths, 2009](https://arxiv.org/html/2605.23054v1#bib.bib62 ""); [Morgan and Levy, 2016](https://arxiv.org/html/2605.23054v1#bib.bib39 "")). Generic collapse predicts tail loss but not the specific functional form.

#### P2: Monotonic regularity increase ( _confirmatory_).

Morphological patterns should regularize across typologically distinct languages, reflecting simplicity bias amplification ( [Shah et al., 2020](https://arxiv.org/html/2605.23054v1#bib.bib12 ""); [Kallini et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib16 "")).

#### P3: Dimension-specific degradation rates ( _partially discriminative_).

Pragmatic constructions should be lost before syntactic ones, reflecting the formal–functional dissociation in LLMs ( [Mahowald et al., 2023](https://arxiv.org/html/2605.23054v1#bib.bib48 "")).

#### P4: Non-monotonic compositionality ( _uniquely discriminative_, critical test).

Without communicative grounding, compositionality should follow a non-monotonic trajectory (initially rising, then falling) even from maximally regular seed data. Only task-grounded evaluation should sustain compositionality ( [Kirby et al., 2015](https://arxiv.org/html/2605.23054v1#bib.bib34 "")). Generic collapse predicts only monotonic degradation.

#### P5: Distributional narrowing ( _confirmatory_).

Zipf exponents should decrease, reflecting tail loss ( [Piantadosi, 2014](https://arxiv.org/html/2605.23054v1#bib.bib49 "")).

We test all five predictions through controlled experiments with two LLMs, including a _regularized-seed control_ and a _three-condition filtering experiment_ that isolate the compression–communication mechanism. Morphological regularity is assessed across English, German, and Turkish; construction diversity and compositionality are evaluated in English with collapse-robust metrics. All five predictions are confirmed. The non-monotonic compositionality trajectory (P4) persists with regularized seed data and is sustained only by quality-grounded (not random) filtering, providing the first LLM-scale demonstration of the compression–communication tradeoff. LLM regularization gradients closely match the human curve from [Morgan and Levy (2016)](https://arxiv.org/html/2605.23054v1#bib.bib39 "").

Our contributions are: (1) an explicit extension of the iterated learning framework of [Ren et al. (2024)](https://arxiv.org/html/2605.23054v1#bib.bib42 "") to natural language, with five falsifiable predictions whose discriminative status is categorized (§ [2](https://arxiv.org/html/2605.23054v1#S2 "2 Theoretical Framework ‣ Model Collapse as Cultural Evolution")); (2) four linguistically grounded metrics with collapse-robust validation (§ [3.4](https://arxiv.org/html/2605.23054v1#S3.SS4 "3.4 Linguistic Metrics ‣ 3 Methods ‣ Model Collapse as Cultural Evolution")); (3) systematic empirical tests including critical controls (regularized-seed, three-condition filter) across 10 generations, two models, and three languages (§ [4](https://arxiv.org/html/2605.23054v1#S4 "4 Results ‣ Model Collapse as Cultural Evolution")); and (4) explicit implications for self-training pipeline design (§ [6](https://arxiv.org/html/2605.23054v1#S6 "6 Discussion ‣ Model Collapse as Cultural Evolution")) and Construction Grammar (Appendix [V](https://arxiv.org/html/2605.23054v1#A22 "Appendix V Discussion: Construction Grammar and Human Parallels ‣ Model Collapse as Cultural Evolution")).

## 2 Theoretical Framework

### 2.1 Iterated Learning and the Compression–Communication Tradeoff

[Griffiths and Kalish (2007)](https://arxiv.org/html/2605.23054v1#bib.bib31 "") proved that when Bayesian learners observe data generated by a previous learner and produce data for the next, the chain of posterior distributions converges to the learner’s prior. [Kalish et al. (2007)](https://arxiv.org/html/2605.23054v1#bib.bib32 "") confirmed this empirically: human participants converged on positive linear functions within 1–4 generations regardless of seed conditions, a result critical for our regularized-seed control design (§ [3.2](https://arxiv.org/html/2605.23054v1#S3.SS2 "3.2 Regularized-Seed Control ‣ 3 Methods ‣ Model Collapse as Cultural Evolution")). [Reali and Griffiths (2009)](https://arxiv.org/html/2605.23054v1#bib.bib62 "") extended this to frequency-dependent regularization under Beta priors, and [Ferdinand et al. (2019)](https://arxiv.org/html/2605.23054v1#bib.bib2 "") demonstrated that these dynamics emerge even with non-Bayesian learners using gradient-based optimization, because the essential mechanism (imperfect learning followed by imperfect reproduction) is shared regardless of the inference procedure.

Three properties are central to our predictions. First, _bottleneck severity_: convergence speed depends on the transmission bottleneck ( [Kirby et al., 2014](https://arxiv.org/html/2605.23054v1#bib.bib33 "")). Second, the _compression–communication tradeoff_: [Kirby et al. (2015)](https://arxiv.org/html/2605.23054v1#bib.bib34 "") demonstrated that transmission chains without communicative pressure produce degenerate languages, while chains with communicative pressure produce compositional languages balancing learnability and expressivity. Third, _dimension-specific emergence_: [Beckner et al. (2017)](https://arxiv.org/html/2605.23054v1#bib.bib63 "") found that structure emerges along some meaning dimensions before others. Concretely, these three properties map onto our predictions as follows: bottleneck severity drives P1 and P5 (the rate and shape of frequency-dependent tail loss); the compression–communication tradeoff drives P2 and P4 (regularization under compression alone vs. the non-monotonic compositionality trajectory that requires communicative pressure to sustain); and dimension-specific emergence drives P3 (the ordering in which constructions are lost). The fine-grained bias–prediction mappings underlying this correspondence are detailed in § [2.2](https://arxiv.org/html/2605.23054v1#S2.SS2 "2.2 LLM Self-Training as Iterated Learning ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution") and Appendix [S](https://arxiv.org/html/2605.23054v1#A19 "Appendix S Bias–Prediction Mapping ‣ Model Collapse as Cultural Evolution").

### 2.2 LLM Self-Training as Iterated Learning

An LLM ℳn\\mathcal{M}\_{n} trained on data DnD\_{n} constitutes generation nn. In self-training, Dn+1D\_{n+1} is sampled from ℳn\\mathcal{M}\_{n}’s output distribution. Each generation implements one step of iterated learning, with the model’s inductive biases playing the role of the Bayesian prior.

[Ren et al. (2024)](https://arxiv.org/html/2605.23054v1#bib.bib42 "") formally established this correspondence, proving that if in-context learning approximates Bayesian inference, the classical convergence result of [Griffiths and Kalish (2007)](https://arxiv.org/html/2605.23054v1#bib.bib31 "") applies: iterative self-training monotonically amplifies prior biases. Our work extends their framework in two directions. First, we characterize which _specific linguistic phenomena_ emerge during this process (non-monotonic compositionality dynamics, frequency-dependent regularization paralleling human acquisition, and dimension-specific construction loss), all invisible under monotonic-amplification models. Second, we test on natural language with weight-based learning (fine-tuning), complementing Ren et al.’s in-context learning experiments.

The mapping between LLM biases and iterated learning priors can be made more precise than a generic “inductive bias” characterization. Following [Ferdinand et al. (2019)](https://arxiv.org/html/2605.23054v1#bib.bib2 "")’s demonstration that different bias types produce different evolutionary trajectories, we identify four specific bias–prediction mappings (detailed in Appendix [S](https://arxiv.org/html/2605.23054v1#A19 "Appendix S Bias–Prediction Mapping ‣ Model Collapse as Cultural Evolution")): _frequency bias_ from next-token training drives P1/P5; _simplicity bias_( [Shah et al., 2020](https://arxiv.org/html/2605.23054v1#bib.bib12 ""); [Kallini et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib16 "")) drives P2; _local coherence bias_ from autoregressive factorization ( [McCoy et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib54 "")) drives P3’s dimension-specific ordering; and _compression without communicative grounding_ drives P4’s non-monotonic compositionality.

We refer to our framework as an _empirically motivated structural correspondence_, not a formal mathematical equivalence, following [McCoy and Griffiths (2025)](https://arxiv.org/html/2605.23054v1#bib.bib73 ""). Critically, [Ferdinand et al. (2019)](https://arxiv.org/html/2605.23054v1#bib.bib2 "") showed that qualitative iterated learning dynamics are robust to non-Bayesian learners, and [Hudson Kam and Newport (2005)](https://arxiv.org/html/2605.23054v1#bib.bib37 "") and [Hudson Kam and Newport (2009)](https://arxiv.org/html/2605.23054v1#bib.bib38 "") demonstrated analogous regularization in human adults. Regarding _bottleneck width_: our 50,000-passage bottleneck is wider than typical human experiments ( [Kirby et al., 2008](https://arxiv.org/html/2605.23054v1#bib.bib61 "")), slowing but not eliminating bias amplification ( [Kirby et al., 2014](https://arxiv.org/html/2605.23054v1#bib.bib33 "")). We adopt the model collapse definition from [Shumailov et al. (2024)](https://arxiv.org/html/2605.23054v1#bib.bib68 ""), noting that [Schaeffer et al. (2025)](https://arxiv.org/html/2605.23054v1#bib.bib67 "") identified eight distinct definitions; our predictions are robust across definitions involving distributional narrowing.

### 2.3 Predictions and Discriminative Status

The five predictions divide into three discriminative classes (Table [10](https://arxiv.org/html/2605.23054v1#A15.T10 "Table 10 ‣ Appendix O Prediction Discriminability Analysis ‣ Model Collapse as Cultural Evolution") in Appendix [O](https://arxiv.org/html/2605.23054v1#A15 "Appendix O Prediction Discriminability Analysis ‣ Model Collapse as Cultural Evolution") gives the full classification with control-experiment results). P2 and P5 follow from generic iterative bias amplification and serve as _confirmatory_ tests verifying our experimental setup—a flat or decreasing regularity in P2, or a stable α\\alpha in P5, would falsify the framework. P1 and P3 are _partially discriminative_: P1 goes beyond generic accounts by predicting a specific log-linear functional form matching human regularization curves ( [Morgan and Levy, 2016](https://arxiv.org/html/2605.23054v1#bib.bib39 "")), not merely that rare items are lost (which any sampling process would produce), while P3 predicts a dimension-specific ordering (pragmatic before structural) reflecting the formal–functional dissociation ( [Mahowald et al., 2023](https://arxiv.org/html/2605.23054v1#bib.bib48 "")). P4 is the _uniquely discriminative_ test: generic model collapse predicts only monotonic degradation, while the compression–communication tradeoff ( [Kirby et al., 2015](https://arxiv.org/html/2605.23054v1#bib.bib34 "")) uniquely predicts an initial rise then fall—a pattern we test with a regularized-seed control to rule out the noise-removal alternative.

## 3 Methods

### 3.1 Self-Training Pipeline

We implement iterated learning with two base models: LLaMA-2-7B ( [Touvron et al., 2023](https://arxiv.org/html/2605.23054v1#bib.bib18 "")) and Mistral-7B ( [Jiang et al., 2023](https://arxiv.org/html/2605.23054v1#bib.bib58 "")), chosen for reproducibility and because their different architectures test generality. Algorithm [1](https://arxiv.org/html/2605.23054v1#algorithm1 "In 3.1 Self-Training Pipeline ‣ 3 Methods ‣ Model Collapse as Cultural Evolution") summarizes the procedure; Figure [1](https://arxiv.org/html/2605.23054v1#S3.F1 "Figure 1 ‣ 3.1 Self-Training Pipeline ‣ 3 Methods ‣ Model Collapse as Cultural Evolution") illustrates the data-vs.-parameter distinction that is the most consequential design choice of the pipeline.

Base model ℳ0\\mathcal{M}\_{0}  (frozen, reused every generation)Generation-nn model ℳn\\mathcal{M}\_{n}Raw outputs Dn+1′D^{\\prime}\_{n+1} (50K passages, τ=0.8\\tau{=}0.8)Filter ℱ∈{\\mathcal{F}\\in\\{none, random 70%, quality top-70%}\\}Training data Dn+1D\_{n+1}fine-tune 3 epochs on DnD\_{n}sample continuationsnext generation

Figure 1: Self-training pipeline. Key design choice: at every generation nn, fine-tuning starts from the _same base model_ ℳ0\\mathcal{M}\_{0} (blue, frozen across the experiment), _not_ from the previous fine-tuned model ℳn−1\\mathcal{M}\_{n-1}. The transmission chain runs through the _data_ (D0→D1→…→D10D\_{0}{\\to}D\_{1}{\\to}\\dots{\\to}D\_{10}; dashed feedback on the left), not through the model parameters. This isolates data-induced degradation from parameter drift and mirrors the iterated-learning paradigm in which each learner begins with the same prior ( [Griffiths and Kalish, 2007](https://arxiv.org/html/2605.23054v1#bib.bib31 "")). Filter ℱ\\mathcal{F} has three settings (§ [3.3](https://arxiv.org/html/2605.23054v1#S3.SS3 "3.3 Three-Condition Filtering Experiment ‣ 3 Methods ‣ Model Collapse as Cultural Evolution")) implementing the compression–communication tradeoff.Algorithm 1Iterated Learning Pipeline for LLM Self-Training. Three filter conditions test the compression–communication tradeoff.

Input:Base model ℳ0\\mathcal{M}\_{0}, seed data D0D\_{0}, generations NN, temperature τ\\tau, filter condition ℱ\\mathcal{F}

Output:Metric trajectories {mn}n=0N\\{m\_{n}\\}\_{n=0}^{N}

1
Compute metrics m0m\_{0} on D0D\_{0};

2for _n=1n=1toNN_ do

3
Generate Dn′D\_{n}^{\\prime} by sampling 50K continuations from ℳn−1\\mathcal{M}\_{n-1} with temperature τ\\tau;

4if _ℱ=\\mathcal{F}= quality_ then

5
Score passages on QA, NLI, summarization;

6Dn←D\_{n}\\leftarrow top 70% of Dn′D\_{n}^{\\prime} by score;

7else if _ℱ=\\mathcal{F}= random_ then

8Dn←D\_{n}\\leftarrow random 70% of Dn′D\_{n}^{\\prime};

9else

10Dn←Dn′D\_{n}\\leftarrow D\_{n}^{\\prime} (no filter);

11
end if

12
Fine-tune ℳ0\\mathcal{M}\_{0} (base model) on DnD\_{n} for 3 epochs →ℳn\\rightarrow\\mathcal{M}\_{n};

13
Compute metrics mnm\_{n} on DnD\_{n} (incl. eRank, posdis diagnostics);

14
end for

#### Generation 0 (seed data).

We use two seed conditions: (i) _natural seed_: 50,000 text passages (100–300 tokens) from a held-out subset of the Pile; (ii) _regularized seed_: 50,000 passages generated from a PCFG engineered for consistent argument structure and regular morphology (§ [3.2](https://arxiv.org/html/2605.23054v1#S3.SS2 "3.2 Regularized-Seed Control ‣ 3 Methods ‣ Model Collapse as Cultural Evolution")).

#### Generations 1–10.

At each generation nn: (i) model ℳn−1\\mathcal{M}\_{n-1} generates 50,000 continuations from 50-token prompts; (ii) the filter condition ℱ\\mathcal{F} is applied; (iii) model ℳn\\mathcal{M}\_{n} is obtained by fine-tuning the _base_ pretrained model on DnD\_{n} for 3 epochs (learning rate 2×10−52{\\times}10^{-5}, batch size 32, AdamW). We fine-tune from the same base model at each generation (not from the previous fine-tuned model) to isolate data degradation from parameter drift, mirroring the iterated learning paradigm where each learner begins with the same prior ( [Griffiths and Kalish, 2007](https://arxiv.org/html/2605.23054v1#bib.bib31 "")). Each condition is run with 5 independent random seeds.

#### Temperature as bottleneck.

We generate with τ=0.8\\tau{=}0.8 and nucleus sampling (p=0.95p{=}0.95) by default. Lower τ\\tau creates tighter bottlenecks; we test τ∈{0.5,0.8,1.0}\\tau\\in\\{0.5,0.8,1.0\\} (§ [4.5](https://arxiv.org/html/2605.23054v1#S4.SS5 "4.5 Sensitivity Analyses: Temperature and Cross-Model ‣ 4 Results ‣ Model Collapse as Cultural Evolution")).

### 3.2 Regularized-Seed Control

To rule out the alternative explanation that P4’s non-monotonic trajectory reflects noise removal from inconsistent seed data rather than compression-driven structure emergence, we create a maximally regular seed corpus. Following [Allen-Zhu and Li (2025)](https://arxiv.org/html/2605.23054v1#bib.bib59 "") and [Kim and Linzen (2020)](https://arxiv.org/html/2605.23054v1#bib.bib19 ""), we generate 50,000 passages from a PCFG ensuring: (i) consistent argument structure (every verb frame is regular), (ii) regular morphology (no irregular forms), and (iii) systematic form–meaning mappings. If the non-monotonic pattern persists from this already-regular starting point, the compression interpretation is confirmed; if compositionality only declines monotonically, the initial rise was noise removal. [Kalish et al. (2007)](https://arxiv.org/html/2605.23054v1#bib.bib32 "") showed that human iterated learning converges to the same attractor regardless of initial conditions; we test whether LLMs exhibit analogous seed-independence.

### 3.3 Three-Condition Filtering Experiment

To isolate communicative pressure from generic diversity preservation, we implement three filter conditions, each modelling a distinct cultural-evolution analogue: (i) no filter retains all generated text (pure transmission, no selection); (ii) random 70% retains a uniformly sampled 70% of passages (uninformed bottleneck—a generic selection pressure that reduces volume but not by communicative criteria); and (iii) quality top-70% retains the top-scoring 70% by independent task evaluation (communicative pressure, following [Kirby et al., 2015](https://arxiv.org/html/2605.23054v1#bib.bib34 "")).

The quality filter uses an independent evaluator (LLaMA-2-13B, larger than the 7B generator) scoring passages on extractive QA, NLI coherence, and summarization fidelity. The choice of these three tasks is principled: each one tests whether the passage successfully communicates content to a downstream reader. Extractive QA verifies that informational content is recoverable from the surface form; NLI coherence checks that propositions inside the passage are mutually consistent (and not internally contradictory in a way only a non-communicating speaker would tolerate); summarization fidelity tests whether the passage retains its meaning under lossy compression—a direct analogue of the listener-reconstruction task that drove compositionality emergence in human iterated-learning experiments ( [Kirby et al., 2015](https://arxiv.org/html/2605.23054v1#bib.bib34 "")). A passage that fails all three lacks the structure required for cooperative information transmission, which is the exact failure mode that the compression-only condition of iterated learning predicts. To rule out same-family distributional bias flagged by [Feng et al. (2025)](https://arxiv.org/html/2605.23054v1#bib.bib9 ""), an additional evaluator-independence check with Flan-T5-XL (a different model family from both generators) confirms the effect is not a distributional-mimicry artifact (Appendix [G](https://arxiv.org/html/2605.23054v1#A7 "Appendix G Evaluator Independence Analysis ‣ Model Collapse as Cultural Evolution")). The critical prediction: random filtering should partially slow collapse (acting as a bottleneck) but should _not_ sustain compositionality; only quality filtering should, paralleling [Kirby et al. (2015)](https://arxiv.org/html/2605.23054v1#bib.bib34 "")’s finding that compositionality requires both transmission and communication pressure. [Gillman et al. (2024)](https://arxiv.org/html/2605.23054v1#bib.bib10 "") showed that expert-knowledge-based correction makes self-consuming loops exponentially more stable, consistent with our quality filter prediction.

### 3.4 Linguistic Metrics

We track four primary metrics, each with collapse-robust validation.

#### Zipf exponent (α\\alpha).

We fit a power-law f⁡(r)∝r−αf(r)\\propto r^{-\\alpha} to the word frequency–rank distribution using maximum likelihood estimation ( [Piantadosi, 2014](https://arxiv.org/html/2605.23054v1#bib.bib49 "")). Following [Clauset et al. (2009)](https://arxiv.org/html/2605.23054v1#bib.bib11 ""), we compare the power-law fit against lognormal and exponential alternatives using likelihood ratio tests. Natural language exhibits α≈1.0\\alpha\\approx 1.0; decreasing α\\alpha indicates distributional narrowing.

#### Morphological regularity (ρM\\rho\_{M}).

We measure the proportion of regular morphological forms in a controlled verb set: 200 English verbs (100 regular, 100 irregular with attested variation), stratified by token frequency. For German (strong/weak verb distinction) and Turkish (vowel harmony), we adapt measures using UniMorph paradigm tables ( [Gutierrez-Vasques and Mijangos, 2020](https://arxiv.org/html/2605.23054v1#bib.bib76 "")). We use the subscript MM to distinguish morphological regularity from Spearman’s rSr\_{S} used in compositionality.

#### Construction diversity (𝒟\\mathcal{D}).

Following [Goldberg (2005)](https://arxiv.org/html/2605.23054v1#bib.bib46 "") and [Bybee (2010)](https://arxiv.org/html/2605.23054v1#bib.bib47 ""), we define 50 syntactic construction types identified via dependency parse patterns. We compute Shannon entropy 𝒟=−∑c∈𝒞p(c)log2p(c)\\mathcal{D}=-\\sum\_{c\\in\\mathcal{C}}p(c)\\log\_{2}p(c) and decompose by frequency quartile to test P1 and P3. Manual validation yields precision ≥0.82\\geq 0.82 across all quartiles (Appendix [B](https://arxiv.org/html/2605.23054v1#A2 "Appendix B Construction Identification Reliability ‣ Model Collapse as Cultural Evolution")).

#### Compositional systematicity (σ\\sigma).

We adapt topographic similarity ( [Brighton and Kirby, 2006](https://arxiv.org/html/2605.23054v1#bib.bib1 "")):

| | | | |
| --- | --- | --- | --- |
| | σ=rS​({dM​(si,sj)},{dF​(fi,fj)})\\sigma=r\_{S}\\bigl(\\{d\_{M}(s\_{i},s\_{j})\\},\\{d\_{F}(f\_{i},f\_{j})\\}\\bigr) | | (1) |

where dMd\_{M} and dFd\_{F} are distances in meaning (PropBank argument overlap) and form (dependency template edit distance) spaces. For instance, the sentences _“Mary gave a book to John”_ and _“The teacher gave a prize to the student”_ share Arg0/Arg1/Arg2 (small dMd\_{M}) and project to the same dependency template nsubj-V-dobj-prep\_to (dF=0d\_{F}=0); high σ\\sigma thus indicates this kind of systematic form–meaning alignment. We complement this with COGS generalization accuracy ( [Kim and Linzen, 2020](https://arxiv.org/html/2605.23054v1#bib.bib19 "")) evaluated via 5-shot prompting (5 in-context examples; see Appendix [D](https://arxiv.org/html/2605.23054v1#A4 "Appendix D COGS Evaluation Methodology ‣ Model Collapse as Cultural Evolution")).

The dependency-template edit-distance metric is reliable when generated text remains within the parser’s syntactic coverage; we monitor coverage via parse-success rate (≥0.94\\geq 0.94 at all generations including generation 10 of unfiltered runs; Appendix [B](https://arxiv.org/html/2605.23054v1#A2 "Appendix B Construction Identification Reliability ‣ Model Collapse as Cultural Evolution")), and cross-validate with the parser-independent posdis and effective rank diagnostics below.

#### Collapse-robust validation.

Topographic similarity can increase when both meaning and form spaces collapse simultaneously ( [Brighton and Kirby, 2006](https://arxiv.org/html/2605.23054v1#bib.bib1 ""); [Chaabouni et al., 2020](https://arxiv.org/html/2605.23054v1#bib.bib13 "")). We validate with three diagnostics: effective rank (eRank; [Roy and Vetterli, 2007](https://arxiv.org/html/2605.23054v1#bib.bib14 "")) computed separately for meaning/form spaces, positional disentanglement (posdis; [Chaabouni et al., 2020](https://arxiv.org/html/2605.23054v1#bib.bib13 "")), and Mantel z-scores (10,000 permutations) following [Kirby et al. (2008)](https://arxiv.org/html/2605.23054v1#bib.bib61 "") and [Galke et al. (2024)](https://arxiv.org/html/2605.23054v1#bib.bib44 ""). Details in Appendix [C](https://arxiv.org/html/2605.23054v1#A3 "Appendix C TopSim Diagnostic Dashboard ‣ Model Collapse as Cultural Evolution").

### 3.5 Human Baselines and Cross-Linguistic Extension

All metrics are computed on three human-written corpora (BNC, OpenWebText, Wikipedia; Appendix [P](https://arxiv.org/html/2605.23054v1#A16 "Appendix P Human Baseline Corpus Details ‣ Model Collapse as Cultural Evolution")). For P1, we overlay frequency-dependent loss data against [Morgan and Levy (2016)](https://arxiv.org/html/2605.23054v1#bib.bib39 "")’s log-linear curve and [Reali and Griffiths (2009)](https://arxiv.org/html/2605.23054v1#bib.bib62 "")’s Beta prior. Morphological experiments are replicated on German (fusional) and Turkish (agglutinative) using UniMorph ( [Gutierrez-Vasques and Mijangos, 2020](https://arxiv.org/html/2605.23054v1#bib.bib76 "")). Construction diversity and compositionality are evaluated in English only, pending broader validated inventories ( [Weissweiler et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib77 "")).

## 4 Results

All reported effect sizes use Hedges’ gg with the small-sample correction J=1−3/(4​df−1)≈0.903J=1-3/(4\\text{df}-1)\\approx 0.903( [Hedges, 1981](https://arxiv.org/html/2605.23054v1#bib.bib51 ""); [Lakens, 2013](https://arxiv.org/html/2605.23054v1#bib.bib52 "")). We report bootstrap-tt 95% CIs (B=10,000B=10{,}000), noting that at n=5n=5, empirical coverage is approximately 81–83% ( [Hesterberg, 2015](https://arxiv.org/html/2605.23054v1#bib.bib53 "")). We additionally report Bayesian 95% highest density intervals (HDIs) with a weakly informative Cauchy(0, 0.707) prior and Bayes factors (BF10\\text{BF}\_{10}) as our primary inferential tool. For cross-condition comparisons, we apply Benjamini–Hochberg FDR correction at q<0.05q<0.05. Individual seed trajectories are plotted alongside means following iterated learning conventions ( [Kirby et al., 2015](https://arxiv.org/html/2605.23054v1#bib.bib34 "")).

### 4.1 P4 (Critical Discriminative Test): The Compression–Communication Tradeoff

We present P4 first because it is the uniquely discriminative test of iterated learning theory.

0011223344556677889910100.20.20.40.4GenerationCompositional Systematicity (σ\\sigma)No filter (natural seed)No filter (regularized seed)Random filterQuality filterFigure 2: Compositional systematicity (σ\\sigma) across generations (LLaMA-2). Four conditions test P4. The non-monotonic trajectory persists with regularized seed data (orange dashed), ruling out the noise-removal alternative. Random filtering (gray dotted) fails to sustain compositionality; only quality filtering (blue) succeeds. Shaded bands: ±1\\pm 1 SD across 5 seeds.

#### Main result.

Figure [2](https://arxiv.org/html/2605.23054v1#S4.F2 "Figure 2 ‣ 4.1 P4 (Critical Discriminative Test): The Compression–Communication Tradeoff ‣ 4 Results ‣ Model Collapse as Cultural Evolution") reveals the non-monotonic trajectory predicted by P4: in the unfiltered condition with natural seed, σ\\sigma increases during generations 0–3 (peaking at 0.47) before declining to 0.31 by generation 10 (Hedges’ g=1.87g=1.87, bootstrap-tt 95% CI \[1.21,2.53\]\[1.21,2.53\], Bayesian HDI \[1.09,2.71\]\[1.09,2.71\], BF10=247\\text{BF}\_{10}=247).

#### Regularized-seed control.

The critical control: with maximally regular seed data, σ\\sigma starts higher (0.52) and still shows a non-monotonic trajectory: a brief plateau followed by a rise to 0.54 at generation 3, then decline to 0.33 by generation 10. The initial compositionality increase occurs even when the seed data is already maximally regular, ruling out the noise-removal alternative explanation and confirming that compression-driven structure reorganization, not noise cleanup, drives the initial rise. The convergence of both conditions toward similar generation-10 values (0.310.31 vs. 0.330.33) is consistent with seed-independent convergence to the prior ( [Kalish et al., 2007](https://arxiv.org/html/2605.23054v1#bib.bib32 ""); [Griffiths and Kalish, 2007](https://arxiv.org/html/2605.23054v1#bib.bib31 "")).

#### Three-condition filtering.

Random filtering produces a trajectory indistinguishable from unfiltered self-training (σ=0.33\\sigma=0.33 at generation 10; p=0.72p=0.72 vs. no filter), while quality filtering sustains compositionality (σ=0.48\\sigma=0.48; p<0.001p<0.001 vs. both other conditions). This directly parallels [Kirby et al. (2015)](https://arxiv.org/html/2605.23054v1#bib.bib34 ""): a generic bottleneck (random filter) does not create the communicative pressure needed for compositionality; only task-grounded evaluation provides this pressure.

#### Collapse-robust validation.

During the compositionality rise (generations 0–3), meaning-space eRank remains stable (12.4→12.112.4\\to 12.1) while σ\\sigma increases, confirming genuine systematicity rather than space collapse. Mantel z-scores exceed the permutation null at all generations (z>3.8z>3.8, p<0.001p<0.001); posdis shows the same non-monotonic trajectory (0.31→0.36→0.220.31\\to 0.36\\to 0.22; Appendix [C](https://arxiv.org/html/2605.23054v1#A3 "Appendix C TopSim Diagnostic Dashboard ‣ Model Collapse as Cultural Evolution")).

| Gen. | Unfiltered | Quality filter |
| --- | --- | --- |
| | σ\\sigma | COGS | σ\\sigma | COGS |
| --- | --- | --- | --- | --- |
| Human∗ | 0.43 | — | — | — |
| Seed | 0.41 | 0.34 | 0.41 | 0.34 |
| 1 | 0.43 | 0.36 | 0.44 | 0.37 |
| 3 | 0.47 | 0.39 | 0.49 | 0.42 |
| 5 | 0.44 | 0.35 | 0.51 | 0.44 |
| 7 | 0.38 | 0.28 | 0.50 | 0.43 |
| 10 | 0.31 | 0.21 | 0.48 | 0.41 |

Table 1: Compositional systematicity (σ\\sigma) and COGS generalization accuracy (LLaMA-2, natural seed). COGS is evaluated via 5-shot prompting (Appendix [D](https://arxiv.org/html/2605.23054v1#A4 "Appendix D COGS Evaluation Methodology ‣ Model Collapse as Cultural Evolution")). Human∗ values are cross-corpus means (Appendix [P](https://arxiv.org/html/2605.23054v1#A16 "Appendix P Human Baseline Corpus Details ‣ Model Collapse as Cultural Evolution")). Both measures confirm the non-monotonic trajectory.

COGS generalization accuracy (Table [1](https://arxiv.org/html/2605.23054v1#S4.T1 "Table 1 ‣ Collapse-robust validation. ‣ 4.1 P4 (Critical Discriminative Test): The Compression–Communication Tradeoff ‣ 4 Results ‣ Model Collapse as Cultural Evolution")) tracks the same non-monotonic pattern (0.34→0.39→0.210.34\\to 0.39\\to 0.21 unfiltered; sustained at 0.410.41 with quality filter), extending emergent communication findings ( [Ren et al., 2020](https://arxiv.org/html/2605.23054v1#bib.bib25 ""); [Chaabouni et al., 2020](https://arxiv.org/html/2605.23054v1#bib.bib13 "")) to full LLM scale.

### 4.2 P1 (Partially Discriminative): Frequency-Dependent Loss Order with Human Comparison

0011223344556677889910102020404060608080100100GenerationNormalized Entropy (%)Q1 (rare)Q2Q3Q4 (frequent)Figure 3: Construction diversity entropy (normalized to Gen. 0 = 100%) by frequency quartile (LLaMA-2, unfiltered). The clean frequency-dependent gradient confirms P1. Shaded region on Q1: ±1\\pm 1 SD across 5 seeds; bands for Q2–Q4 omitted for clarity (all SD ≤0.02\\leq 0.02).

Figure [3](https://arxiv.org/html/2605.23054v1#S4.F3 "Figure 3 ‣ 4.2 P1 (Partially Discriminative): Frequency-Dependent Loss Order with Human Comparison ‣ 4 Results ‣ Model Collapse as Cultural Evolution") reveals the frequency-dependent pattern predicted by P1: the rarest quartile (Q1) retains only 32% of its original entropy by generation 10, while the most frequent (Q4) retains 88% (Hedges’ g=3.08g=3.08, bootstrap-tt CI \[2.07,4.09\]\[2.07,4.09\], BF10>1000\\text{BF}\_{10}>1000).

The discriminative test for P1 is whether the gradient’s _functional form_ matches human regularization, not merely that frequency-dependent loss exists. The LLM gradient closely matches [Morgan and Levy (2016)](https://arxiv.org/html/2605.23054v1#bib.bib39 "")’s log-linear curve (R2=0.94R^{2}=0.94; Figure [4](https://arxiv.org/html/2605.23054v1#A21.F4 "Figure 4 ‣ Appendix U Human Regularization Overlay ‣ Model Collapse as Cultural Evolution"), Appendix [U](https://arxiv.org/html/2605.23054v1#A21 "Appendix U Human Regularization Overlay ‣ Model Collapse as Cultural Evolution")), consistent with their finding that frequency-dependent regularization emerges from a frequency- _independent_ bias interacting with a transmission bottleneck. The fit is comparable to the Beta(α/2,α/2\\alpha/2,\\alpha/2) prior with α/2≈0.03\\alpha/2\\approx 0.03 from [Reali and Griffiths (2009)](https://arxiv.org/html/2605.23054v1#bib.bib62 "").

The constructions lost first are those requiring pragmatic or discourse-level competence (left-dislocation, clefts, rhetorical questions), while core syntactic constructions (simple transitive, copular) persist, simultaneously confirming P3. We define _pragmatic_ constructions as those whose felicity depends on discourse context, speaker intent, or information structure—clefts mark contrastive focus, left-dislocations mark topic, rhetorical questions perform non-question speech acts—whereas _structural_ (syntactic) constructions are licensed by purely formal grammatical patterns and remain felicitous regardless of context (simple transitive, copular, ditransitive). Morphological constructions (passive, comparative) fall in between, requiring some functional sensitivity but anchored in formal patterns. The full inventory of 50 construction types, organized by this distinction, is in Appendix [A](https://arxiv.org/html/2605.23054v1#A1 "Appendix A Construction Inventory ‣ Model Collapse as Cultural Evolution"); reliability of automatic identification (precision ≥0.82\\geq 0.82 in the rarest quartile) is in Appendix [B](https://arxiv.org/html/2605.23054v1#A2 "Appendix B Construction Identification Reliability ‣ Model Collapse as Cultural Evolution"). This ordering connects to the formal–functional dissociation ( [Mahowald et al., 2023](https://arxiv.org/html/2605.23054v1#bib.bib48 "")): constructions relying on formal competence survive; those requiring functional competence are lost first.

### 4.3 P3 (Partially Discriminative): Dimension-Specific Degradation Rates

The dimension-specific ordering predicted by P3 is quantified through the correlation between CxG entrenchment ranking and survival generation across the 50 construction types: r=0.73r=0.73 (p<0.001p<0.001; Hedges’ g=2.11g=2.11, bootstrap-tt CI \[1.42,2.80\]\[1.42,2.80\], BF10>1000\\text{BF}\_{10}>1000). Pragmatic constructions (mean survival: generation 4.2) are lost significantly earlier than syntactic ones (generation 8.7), with morphological constructions intermediate (generation 6.1).

This three-way ordering admits two convergent theoretical interpretations. First, from a Construction Grammar _entrenchment_ perspective ( [Goldberg, 2005](https://arxiv.org/html/2605.23054v1#bib.bib46 ""); [Bybee, 2010](https://arxiv.org/html/2605.23054v1#bib.bib47 "")): constructions with high type frequency develop strong network connections to their open argument slots, making them robust under reduced input; low-frequency constructions, lacking this entrenchment, lose their productivity signal first. The Pearson correlation r=0.73r=0.73 between log-type-frequency and survival generation (Appendix [N](https://arxiv.org/html/2605.23054v1#A14 "Appendix N CxG Entrenchment Analysis Details ‣ Model Collapse as Cultural Evolution")) is the quantitative signature of this effect. Second, from a _formal–functional dissociation_ perspective ( [Mahowald et al., 2023](https://arxiv.org/html/2605.23054v1#bib.bib48 "")): LLMs distinguish formal linguistic competence (producing well-formed strings) from functional competence (using language for pragmatically appropriate ends). Pragmatic constructions—clefts, rhetorical questions, left-dislocations—require functional competence beyond formal pattern-matching, and are precisely the ones that degrade first. The two perspectives converge on the observed ordering: entrenched type-frequent patterns are formally robust, while pragmatic constructions require functional competence that exceeds formal patterns. Iterated self-training erodes both in the predicted order—a result that generic model collapse, which predicts uniform degradation, cannot explain.

### 4.4 P2 and P5 (Confirmatory): Regularity Increase and Distributional Narrowing

| Gen. | ρM​-EN\\rho\_{M\\text{-EN}} | Δ\\DeltaIrreg. | ρM​-DE\\rho\_{M\\text{-DE}} | ρM​-TR\\rho\_{M\\text{-TR}} |
| --- | --- | --- | --- | --- |
| Human∗ | 0.61 | — | 0.47 | 0.69 |
| Seed | 0.62 | — | 0.48 | 0.71 |
| 1 | 0.64 | −3.1%-3.1\\% | 0.49 | 0.73 |
| 3 | 0.69 | −11.2%-11.2\\% | 0.53 | 0.77 |
| 5 | 0.75 | −21.6%-21.6\\% | 0.58 | 0.82 |
| 7 | 0.80 | −30.4%-30.4\\% | 0.63 | 0.86 |
| 10 | 0.87 | −42.7%-42.7\\% | 0.70 | 0.91 |
| 10QF | 0.71 | −15.3%-15.3\\% | 0.55 | 0.79 |

Table 2: Morphological regularity (ρM\\rho\_{M}) across three languages. QF: quality-filtered. Regularity increases monotonically; low-frequency irregulars regularize first (consistent with P1). Human∗ = cross-corpus means.

Morphological regularity increases monotonically (Table [2](https://arxiv.org/html/2605.23054v1#S4.T2 "Table 2 ‣ 4.4 P2 and P5 (Confirmatory): Regularity Increase and Distributional Narrowing ‣ 4 Results ‣ Model Collapse as Cultural Evolution")), confirming P2 (Hedges’ g=4.27g=4.27, bootstrap-tt CI \[2.89,5.65\]\[2.89,5.65\], BF10>1000\\text{BF}\_{10}>1000). By generation 10, irregular verb forms decline by 42.7% in English. Regularization matches usage-based predictions ( [Bybee, 2010](https://arxiv.org/html/2605.23054v1#bib.bib47 "")): low-frequency irregulars ( _wrung_ →\\to _\*wringed_) regularize by generation 3, while high-frequency ones ( _went_) resist until generation 10 (94% in syntactically appropriate contexts; Appendix [M](https://arxiv.org/html/2605.23054v1#A13 "Appendix M Regularization Examples with Syntactic Context ‣ Model Collapse as Cultural Evolution")). Cross-linguistically, German rises more slowly (0.48→0.700.48\\to 0.70) due to richer paradigms; Turkish (0.71→0.910.71\\to 0.91) reaches ceiling effects quickly ( [Lupyan and Dale, 2010](https://arxiv.org/html/2605.23054v1#bib.bib56 ""); [Culbertson, 2010](https://arxiv.org/html/2605.23054v1#bib.bib64 "")).

The Zipf exponent decreases monotonically (α:1.07→0.82\\alpha:1.07\\to 0.82, LLaMA-2; Appendix [T](https://arxiv.org/html/2605.23054v1#A20 "Appendix T Full Zipf Exponent Data ‣ Model Collapse as Cultural Evolution")), confirming P5 (g=1.93g=1.93, BF10=189\\text{BF}\_{10}=189). The power-law fit is preferred at all generations (Δ\\DeltaAIC >4>4; Appendix [I](https://arxiv.org/html/2605.23054v1#A9 "Appendix I Zipf Goodness-of-Fit ‣ Model Collapse as Cultural Evolution")). Mistral shows the same pattern (α:1.07→0.86\\alpha:1.07\\to 0.86); quality filtering preserves diversity (α=0.97\\alpha=0.97).

### 4.5 Sensitivity Analyses: Temperature and Cross-Model

We confirm the predicted parametric relationship between bottleneck severity and convergence speed ( [Kirby et al., 2014](https://arxiv.org/html/2605.23054v1#bib.bib33 "")): lowering temperature from τ=1.0\\tau=1.0 to τ=0.5\\tau=0.5 shifts the P4 peak from generation 4 to generation 2; a 10×10\\times narrower bottleneck (5K vs. 50K passages) shifts it to generation 1–2 (Appendix [K](https://arxiv.org/html/2605.23054v1#A11 "Appendix K Temperature as Bottleneck Severity: Full Results ‣ Model Collapse as Cultural Evolution")).

Mistral-7B replicates all five predictions with the same qualitative structure and similar effect sizes (Appendix [Q](https://arxiv.org/html/2605.23054v1#A17 "Appendix Q Full Mistral-7B Results ‣ Model Collapse as Cultural Evolution")). Key numbers track LLaMA-2 closely: P4 peak at generation 3 (σmax=0.48\\sigma\_{\\max}{=}0.48 vs. LLaMA-2’s 0.47), quality filtering sustains σ=0.47\\sigma{=}0.47 at generation 10 (vs. 0.48), Zipf α\\alpha decreases 1.07→0.861.07{\\to}0.86 (vs. 1.07→0.821.07{\\to}0.82), and the cross-linguistic ordering Turkish >> English >> German appears in morphological regularization. The qualitative invariance under architecture change confirms general iterated-learning properties, not architecture-specific artifacts ( [Griffiths and Kalish, 2007](https://arxiv.org/html/2605.23054v1#bib.bib31 "")).

## 5 Related Work

#### Model collapse.

A statistical characterization of model collapse has emerged from converging analyses: irreversible tail loss ( [Shumailov et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib68 "")), self-consuming-loop formalism ( [Alemohammad et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib3 "")), scaling-law effects ( [Dohmatob et al., 2024b](https://arxiv.org/html/2605.23054v1#bib.bib4 "")), regression-setting analyses ( [Dohmatob et al., 2024a](https://arxiv.org/html/2605.23054v1#bib.bib5 "")), and strong collapse from small synthetic fractions ( [Dohmatob et al., 2025](https://arxiv.org/html/2605.23054v1#bib.bib6 "")). Adjacent findings include the persistence of correctness alongside diversity decline ( [Briesch et al., 2023](https://arxiv.org/html/2605.23054v1#bib.bib8 "")), the protective effect of data accumulation ( [Gerstgrasser et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib65 "")), information-theoretic accounts ( [Seddik et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib41 "")), dataset-bias amplification ( [Taori and Hashimoto, 2023](https://arxiv.org/html/2605.23054v1#bib.bib7 "")), and the verification-quality phase transition ( [Feng et al., 2025](https://arxiv.org/html/2605.23054v1#bib.bib9 "")). [Schaeffer et al. (2025)](https://arxiv.org/html/2605.23054v1#bib.bib67 "") catalogued eight distinct collapse definitions (we adopt that of [Shumailov et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib68 "")). The closest precedent to our program is [Guo et al. (2024)](https://arxiv.org/html/2605.23054v1#bib.bib66 ""), who measured linguistic-diversity decline across several dimensions but without an evolutionary framework or discriminative theory test.

#### Cultural evolution and LLMs.

A growing body of work connects LLM training dynamics to iterated learning. [Ren et al. (2024)](https://arxiv.org/html/2605.23054v1#bib.bib42 "") formally instantiated LLM self-evolution as Bayesian iterated learning and proved monotonic bias amplification; [Shumailov et al. (2024)](https://arxiv.org/html/2605.23054v1#bib.bib68 "") argued in _Nature_ that the compression–expressivity tradeoff explains why self-training degrades. Empirical tests at smaller scales include emergent communication ( [Ren et al., 2020](https://arxiv.org/html/2605.23054v1#bib.bib25 ""); [Chaabouni et al., 2020](https://arxiv.org/html/2605.23054v1#bib.bib13 "")), language evolution in LLM populations ( [Perez et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib43 "")), learnability advantages of compositional structure ( [Galke et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib44 ""); [Galke et al., 2023](https://arxiv.org/html/2605.23054v1#bib.bib71 "")), degenerate vocabularies arising without compression pressure ( [Kouwenhoven et al., 2025b](https://arxiv.org/html/2605.23054v1#bib.bib69 "")), comparisons of human/LLM/hybrid conditions ( [Kouwenhoven et al., 2025a](https://arxiv.org/html/2605.23054v1#bib.bib70 "")), iterated learning improving CLIP compositionality ( [Zheng et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib45 "")), and elicitation of LLM priors via iterated in-context learning ( [Zhu and Griffiths, 2024](https://arxiv.org/html/2605.23054v1#bib.bib72 "")). Extended related work on compositionality benchmarks, emergent communication, and inductive biases is provided in Appendix [W](https://arxiv.org/html/2605.23054v1#A23 "Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution").

## 6 Discussion

#### Summary of findings.

Iterated learning theory fills the explanatory gap left by existing statistical accounts of model collapse. The five predictions derived from cultural evolution (frequency-dependent loss, regularization, dimension-specific degradation, non-monotonic compositionality, and distributional narrowing) are confirmed across two architectures, three typologically distinct languages, and multiple controls, with large effect sizes. The critical discriminative result is the non-monotonic compositionality trajectory, which persists under maximally regular seed data (ruling out noise-removal) and is sustained only by quality-grounded filtering, demonstrating at LLM scale that the compression–communication tradeoff ( [Kirby et al., 2015](https://arxiv.org/html/2605.23054v1#bib.bib34 "")) governs the emergence and loss of linguistic structure in self-training.

#### Engagement with linguistic theory.

The results bear directly on three theoretical traditions that have evolved largely in parallel. From _cultural evolution_, the close match between LLM regularization gradients and the human curve of [Morgan and Levy (2016)](https://arxiv.org/html/2605.23054v1#bib.bib39 "") (R2=0.94R^{2}=0.94) supports the hypothesis that frequency-dependent regularization emerges from a frequency- _independent_ simplicity bias interacting with a transmission bottleneck ( [Ferdinand et al., 2019](https://arxiv.org/html/2605.23054v1#bib.bib2 "")), not from any human-specific cognitive architecture. From _Construction Grammar_, the r=0.73r=0.73 correlation between log-type-frequency and survival generation (§ [4](https://arxiv.org/html/2605.23054v1#S4 "4 Results ‣ Model Collapse as Cultural Evolution"), Appendix [N](https://arxiv.org/html/2605.23054v1#A14 "Appendix N CxG Entrenchment Analysis Details ‣ Model Collapse as Cultural Evolution")) is a direct evolutionary test of the entrenchment hypothesis ( [Goldberg, 2005](https://arxiv.org/html/2605.23054v1#bib.bib46 ""); [Bybee, 2010](https://arxiv.org/html/2605.23054v1#bib.bib47 "")); the three-way ordering (pragmatic << morphological << structural) extends entrenchment from a static productivity property to a dynamic resilience-under-transmission property. From the _formal–functional dissociation_ literature, the same ordering follows independently from [Mahowald et al. (2023)](https://arxiv.org/html/2605.23054v1#bib.bib48 "")’s prediction that LLMs prioritize formal over functional competence; the convergence of two perspectives on the same observed ordering is itself novel evidence that entrenchment is at least partly a formal-competence phenomenon. Conversely, [Ren et al. (2024)](https://arxiv.org/html/2605.23054v1#bib.bib42 "")’s monotonic-amplification result does not predict our non-monotonic trajectory; reconciling the two requires moving from in-context learning (where weights are fixed) to weight-based fine-tuning, where compression-induced reorganization can momentarily increase systematicity before convergence to the prior.

#### Implications and reconciliation of concurrent results.

The compression–communication framework offers a unifying explanation for several recent findings. The degenerate vocabularies of [Kouwenhoven et al. (2025b)](https://arxiv.org/html/2605.23054v1#bib.bib69 "") in in-context iterated learning, and the LLM-optimized degeneracy of [Kouwenhoven et al. (2025a)](https://arxiv.org/html/2605.23054v1#bib.bib70 ""), both instantiate compression without communicative pressure—the condition the tradeoff predicts will produce collapse. The same principle explains why pure self-training degrades while Constitutional AI ( [Bai et al., 2022](https://arxiv.org/html/2605.23054v1#bib.bib28 "")) and self-play ( [Chen et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib29 "")) succeed: only quality-grounded filtering supplies the communicative pressure needed to sustain structured output, consistent with the verification-quality phase transition of [Feng et al. (2025)](https://arxiv.org/html/2605.23054v1#bib.bib9 ""). Data accumulation ( [Gerstgrasser et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib65 "")) prevents collapse through a mechanism analogous to diverse speaker populations in human cultural evolution ( [Raviv et al., 2019](https://arxiv.org/html/2605.23054v1#bib.bib57 "")). Three pipeline-design principles follow: use task-grounded (not random) filtering as the verification signal; prefer a different-family evaluator to avoid distributional mimicry; and treat bottleneck width as a tunable governing convergence rate to the prior. All materials—training pipeline, statistical analysis code, regularized-seed PCFG, and configuration files—are publicly available at [https://github.com/bettyguo/iterated-collapse](https://github.com/bettyguo/iterated-collapse "").

## Acknowledgments

We thank the anonymous CoNLL 2026 reviewers and the area chair for their detailed and constructive feedback, which substantially improved the clarity of the theoretical framework, the methodology section, and the discussion of Construction Grammar parallels. We also thank the developers of the LLaMA-2, Mistral, and Flan-T5 model families for releasing their weights, and the maintainers of the UniMorph, COGS, PropBank, and Universal Dependencies resources upon which our analyses depend. Computational resources were provided by The University of Hong Kong.

## 7 Limitations

We acknowledge six specific limitations. (1) The theoretical framework is an empirically motivated structural correspondence, not a formal mathematical equivalence; conditions under which SGD fine-tuning approximates Bayesian posterior sampling remain open. (2) Construction diversity and compositionality are tested only in English; cross-linguistic testing awaits broader validated inventories such as UCxn ( [Weissweiler et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib77 "")). (3) The task-grounded evaluator is a unilateral quality filter, not an interactive dialogue partner; while evaluator independence checks with Flan-T5-XL mitigate model-family confounds, future work should test human evaluators and interactive settings. (4) We test 7B-parameter models with a 50,000-passage bottleneck (1,000×1{,}000\\times larger than typical human experiments); although our parametric analyses show predicted effects, formal quantitative extrapolation and scaling to larger models require validation. (5) Our human comparison uses published data from [Morgan and Levy (2016)](https://arxiv.org/html/2605.23054v1#bib.bib39 "") and [Reali and Griffiths (2009)](https://arxiv.org/html/2605.23054v1#bib.bib62 ""); future work should run parallel human and LLM iterated learning experiments. (6) The quality filter aggregates QA, NLI, and summarization scores into a single signal; because each task emphasizes a different aspect of communicative success (information recoverability, internal consistency, compression-resistance), different task mixes may preserve different linguistic structures; this ablation we leave to future work.

## References

- Alemohammad et al. (2024)S. Alemohammad, J. Casco-Rodriguez, L. Luzi, A. I. Humayun, H. Babaei, D. LeJeune, A. Siahkoohi, and R. G. BaraniukSelf-consuming generative models go MAD.
In The Twelfth International Conference on Learning Representations,
ICLR 2024, Vienna, Austria, May 7-11, 2024,
Cited by: [§1](https://arxiv.org/html/2605.23054v1#S1.p2.1 "1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px1.p1.1 "Model collapse. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution").

- Allen-Zhu and Li (2025)Z. Allen-Zhu and Y. LiPhysics of language models: part 1, learning hierarchical language structures.
Trans. Mach. Learn. Res.2025.
Cited by: [§3.2](https://arxiv.org/html/2605.23054v1#S3.SS2.p1.1 "3.2 Regularized-Seed Control ‣ 3 Methods ‣ Model Collapse as Cultural Evolution").

- Bai et al. (2022)Y. Bai, S. Kadavath, S. Kundu, A. Askell, J. Kernion, A. Jones, A. Chen, A. Goldie, A. Mirhoseini, C. McKinnon, C. Chen, C. Olsson, C. Olah, D. Hernandez, D. Drain, D. Ganguli, D. Li, E. Tran-Johnson, E. Perez, J. Kerr, J. Mueller, J. Ladish, J. Landau, K. Ndousse, K. Lukosiute, L. Lovitt, M. Sellitto, N. Elhage, N. Schiefer, N. Mercado, N. DasSarma, R. Lasenby, R. Larson, S. Ringer, S. Johnston, S. Kravec, S. E. Showk, S. Fort, T. Lanham, T. Telleen-Lawton, T. Conerly, T. Henighan, T. Hume, S. R. Bowman, Z. Hatfield-Dodds, B. Mann, D. Amodei, N. Joseph, S. McCandlish, T. Brown, and J. KaplanConstitutional AI: harmlessness from AI feedback.
arXiv preprintarXiv.2212.08073.
External Links: [Document](https://dx.doi.org/10.48550/ARXIV.2212.08073 "")Cited by: [§6](https://arxiv.org/html/2605.23054v1#S6.SS0.SSS0.Px3.p1.1 "Implications and reconciliation of concurrent results. ‣ 6 Discussion ‣ Model Collapse as Cultural Evolution").

- Beckner et al. (2017)C. Beckner, J. B. Pierrehumbert, and J. HayThe emergence of linguistic structure in an online iterated learning task.
Journal of Language Evolution2 (2), pp. 160–176.
External Links: ISSN 2058-4571,
[Document](https://dx.doi.org/10.1093/jole/lzx001 ""),
[Link](https://doi.org/10.1093/jole/lzx001 "")Cited by: [§2.1](https://arxiv.org/html/2605.23054v1#S2.SS1.p2.1 "2.1 Iterated Learning and the Compression–Communication Tradeoff ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution").

- Briesch et al. (2023)M. Briesch, D. Sobania, and F. RothlaufLarge language models suffer from their own output: an analysis of the self-consuming training loop.
arXiv preprintarXiv.2311.16822.
External Links: [Document](https://dx.doi.org/10.48550/ARXIV.2311.16822 "")Cited by: [§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px1.p1.1 "Model collapse. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution").

- Brighton and Kirby (2006)H. Brighton and S. KirbyUnderstanding linguistic evolution by visualizing the emergence of topographic mappings.
Artif. Life12 (2), pp. 229–242.
External Links: [Document](https://dx.doi.org/10.1162/ARTL.2006.12.2.229 "")Cited by: [§3.4](https://arxiv.org/html/2605.23054v1#S3.SS4.SSS0.Px4.p1.1 "Compositional systematicity (𝜎). ‣ 3.4 Linguistic Metrics ‣ 3 Methods ‣ Model Collapse as Cultural Evolution"),
[§3.4](https://arxiv.org/html/2605.23054v1#S3.SS4.SSS0.Px5.p1.1 "Collapse-robust validation. ‣ 3.4 Linguistic Metrics ‣ 3 Methods ‣ Model Collapse as Cultural Evolution").

- Bybee (2010)J. BybeeLanguage, usage and cognition.
Cambridge University Press.
External Links: ISBN 9780511750526,
[Document](https://dx.doi.org/10.1017/cbo9780511750526 "")Cited by: [Appendix N](https://arxiv.org/html/2605.23054v1#A14.p1.1 "Appendix N CxG Entrenchment Analysis Details ‣ Model Collapse as Cultural Evolution"),
[Appendix V](https://arxiv.org/html/2605.23054v1#A22.p2.1 "Appendix V Discussion: Construction Grammar and Human Parallels ‣ Model Collapse as Cultural Evolution"),
[§3.4](https://arxiv.org/html/2605.23054v1#S3.SS4.SSS0.Px3.p1.1 "Construction diversity (𝒟). ‣ 3.4 Linguistic Metrics ‣ 3 Methods ‣ Model Collapse as Cultural Evolution"),
[§4.3](https://arxiv.org/html/2605.23054v1#S4.SS3.p2.1 "4.3 P3 (Partially Discriminative): Dimension-Specific Degradation Rates ‣ 4 Results ‣ Model Collapse as Cultural Evolution"),
[§4.4](https://arxiv.org/html/2605.23054v1#S4.SS4.p1.1 "4.4 P2 and P5 (Confirmatory): Regularity Increase and Distributional Narrowing ‣ 4 Results ‣ Model Collapse as Cultural Evolution"),
[§6](https://arxiv.org/html/2605.23054v1#S6.SS0.SSS0.Px2.p1.1 "Engagement with linguistic theory. ‣ 6 Discussion ‣ Model Collapse as Cultural Evolution").

- Chaabouni et al. (2020)R. Chaabouni, E. Kharitonov, D. Bouchacourt, E. Dupoux, and M. BaroniCompositionality and generalization in emergent languages.
In Proceedings of the 58th Annual Meeting of the Association for Computational
Linguistics, ACL 2020, Online, July 5-10, 2020, D. Jurafsky, J. Chai, N. Schluter, and J. R. Tetreault (Eds.),
pp. 4427–4442.
External Links: [Document](https://dx.doi.org/10.18653/V1/2020.ACL-MAIN.407 "")Cited by: [Appendix W](https://arxiv.org/html/2605.23054v1#A23.SS0.SSS0.Px1.p1.1 "Compositionality and inductive biases. ‣ Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution"),
[Appendix C](https://arxiv.org/html/2605.23054v1#A3.p1.1 "Appendix C TopSim Diagnostic Dashboard ‣ Model Collapse as Cultural Evolution"),
[§3.4](https://arxiv.org/html/2605.23054v1#S3.SS4.SSS0.Px5.p1.1 "Collapse-robust validation. ‣ 3.4 Linguistic Metrics ‣ 3 Methods ‣ Model Collapse as Cultural Evolution"),
[§4.1](https://arxiv.org/html/2605.23054v1#S4.SS1.SSS0.Px4.p2.1 "Collapse-robust validation. ‣ 4.1 P4 (Critical Discriminative Test): The Compression–Communication Tradeoff ‣ 4 Results ‣ Model Collapse as Cultural Evolution"),
[§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px2.p1.1 "Cultural evolution and LLMs. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution").

- Chen et al. (2024)Z. Chen, Y. Deng, H. Yuan, K. Ji, and Q. GuSelf-play fine-tuning converts weak language models to strong language models.
In Forty-first International Conference on Machine Learning, ICML 2024,
Vienna, Austria, July 21-27, 2024, R. Salakhutdinov, Z. Kolter, K. A. Heller, A. Weller, N. Oliver, J. Scarlett, and F. Berkenkamp (Eds.),
Proceedings of Machine Learning Research, Vol. 235, pp. 6621–6642.
Cited by: [§6](https://arxiv.org/html/2605.23054v1#S6.SS0.SSS0.Px3.p1.1 "Implications and reconciliation of concurrent results. ‣ 6 Discussion ‣ Model Collapse as Cultural Evolution").

- Christiansen and Chater (2015)M. H. Christiansen and N. ChaterThe now-or-never bottleneck: a fundamental constraint on language.
Behavioral and Brain Sciences39.
External Links: ISSN 1469-1825,
[Document](https://dx.doi.org/10.1017/s0140525x1500031x "")Cited by: [§1](https://arxiv.org/html/2605.23054v1#S1.p1.1 "1 Introduction ‣ Model Collapse as Cultural Evolution").

- Christiansen and Chater (2016)M. H. Christiansen and N. ChaterLanguage as shaped by the brain.
In Creating Language,
pp. 19–65.
External Links: [Document](https://dx.doi.org/10.7551/mitpress/9780262034319.003.0002 "")Cited by: [§1](https://arxiv.org/html/2605.23054v1#S1.p1.1 "1 Introduction ‣ Model Collapse as Cultural Evolution").

- Chung et al. (2024)H. W. Chung, L. Hou, S. Longpre, B. Zoph, Y. Tay, W. Fedus, Y. Li, X. Wang, M. Dehghani, S. Brahma, A. Webson, S. S. Gu, Z. Dai, M. Suzgun, X. Chen, A. Chowdhery, A. Castro-Ros, M. Pellat, K. Robinson, D. Valter, S. Narang, G. Mishra, A. Yu, V. Y. Zhao, Y. Huang, A. M. Dai, H. Yu, S. Petrov, E. H. Chi, J. Dean, J. Devlin, A. Roberts, D. Zhou, Q. V. Le, and J. WeiScaling instruction-finetuned language models.
J. Mach. Learn. Res.25, pp. 70:1–70:53.
Cited by: [Appendix G](https://arxiv.org/html/2605.23054v1#A7.p1.1 "Appendix G Evaluator Independence Analysis ‣ Model Collapse as Cultural Evolution").

- Clauset et al. (2009)A. Clauset, C. R. Shalizi, and M. E. J. NewmanPower-law distributions in empirical data.
SIAM Rev.51 (4), pp. 661–703.
External Links: [Document](https://dx.doi.org/10.1137/070710111 "")Cited by: [Table 12](https://arxiv.org/html/2605.23054v1#A20.T12 "In Appendix T Full Zipf Exponent Data ‣ Model Collapse as Cultural Evolution"),
[Appendix I](https://arxiv.org/html/2605.23054v1#A9.p1.1 "Appendix I Zipf Goodness-of-Fit ‣ Model Collapse as Cultural Evolution"),
[§3.4](https://arxiv.org/html/2605.23054v1#S3.SS4.SSS0.Px1.p1.1 "Zipf exponent (𝛼). ‣ 3.4 Linguistic Metrics ‣ 3 Methods ‣ Model Collapse as Cultural Evolution").

- Culbertson and Adger (2014)J. Culbertson and D. AdgerLanguage learners privilege structured meaning over surface frequency.
Proceedings of the National Academy of Sciences111 (16), pp. 5842–5847.
External Links: ISSN 1091-6490,
[Document](https://dx.doi.org/10.1073/pnas.1320525111 "")Cited by: [Appendix V](https://arxiv.org/html/2605.23054v1#A22.p1.1 "Appendix V Discussion: Construction Grammar and Human Parallels ‣ Model Collapse as Cultural Evolution").

- Culbertson (2010)J. CulbertsonLearning biases, regularization, and the emergence of typological universals in syntax.
Ph.D. Thesis, Johns Hopkins University, Baltimore, MD.
Note: ProQuest LLC, ERIC ED523070Cited by: [§4.4](https://arxiv.org/html/2605.23054v1#S4.SS4.p1.1 "4.4 P2 and P5 (Confirmatory): Regularity Increase and Distributional Narrowing ‣ 4 Results ‣ Model Collapse as Cultural Evolution").

- Dohmatob et al. (2024a)E. Dohmatob, Y. Feng, and J. KempeModel collapse demystified: the case of regression.
In Advances in Neural Information Processing Systems 38: Annual Conference
on Neural Information Processing Systems 2024, NeurIPS 2024, Vancouver,
BC, Canada, December 10 - 15, 2024, A. Globersons, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. M. Tomczak, and C. Zhang (Eds.),
Cited by: [§1](https://arxiv.org/html/2605.23054v1#S1.p2.1 "1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px1.p1.1 "Model collapse. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution").

- Dohmatob et al. (2025)E. Dohmatob, Y. Feng, A. Subramonian, and J. KempeStrong model collapse.
In The Thirteenth International Conference on Learning Representations,
ICLR 2025, Singapore, April 24-28, 2025,
Cited by: [§1](https://arxiv.org/html/2605.23054v1#S1.p2.1 "1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px1.p1.1 "Model collapse. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution").

- Dohmatob et al. (2024b)E. Dohmatob, Y. Feng, P. Yang, F. Charton, and J. KempeA tale of tails: model collapse as a change of scaling laws.
In Forty-first International Conference on Machine Learning, ICML 2024,
Vienna, Austria, July 21-27, 2024, R. Salakhutdinov, Z. Kolter, K. A. Heller, A. Weller, N. Oliver, J. Scarlett, and F. Berkenkamp (Eds.),
Proceedings of Machine Learning Research, Vol. 235, pp. 11165–11197.
Cited by: [§1](https://arxiv.org/html/2605.23054v1#S1.p2.1 "1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px1.p1.1 "Model collapse. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution").

- Feng et al. (2025)Y. Feng, E. Dohmatob, P. Yang, F. Charton, and J. KempeBeyond model collapse: scaling up with synthesized data requires verification.
In The Thirteenth International Conference on Learning Representations,
ICLR 2025, Singapore, April 24-28, 2025,
Cited by: [§3.3](https://arxiv.org/html/2605.23054v1#S3.SS3.p2.1 "3.3 Three-Condition Filtering Experiment ‣ 3 Methods ‣ Model Collapse as Cultural Evolution"),
[§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px1.p1.1 "Model collapse. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution"),
[§6](https://arxiv.org/html/2605.23054v1#S6.SS0.SSS0.Px3.p1.1 "Implications and reconciliation of concurrent results. ‣ 6 Discussion ‣ Model Collapse as Cultural Evolution").

- Ferdinand et al. (2019)V. Ferdinand, S. Kirby, and K. SmithThe cognitive roots of regularization in language.
Cognition184, pp. 53–68.
External Links: ISSN 0010-0277,
[Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.cognition.2018.12.002 ""),
[Link](https://www.sciencedirect.com/science/article/pii/S0010027718303135 "")Cited by: [Appendix S](https://arxiv.org/html/2605.23054v1#A19.p1.1 "Appendix S Bias–Prediction Mapping ‣ Model Collapse as Cultural Evolution"),
[§2.1](https://arxiv.org/html/2605.23054v1#S2.SS1.p1.1 "2.1 Iterated Learning and the Compression–Communication Tradeoff ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution"),
[§2.2](https://arxiv.org/html/2605.23054v1#S2.SS2.p3.1 "2.2 LLM Self-Training as Iterated Learning ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution"),
[§2.2](https://arxiv.org/html/2605.23054v1#S2.SS2.p4.1 "2.2 LLM Self-Training as Iterated Learning ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution"),
[§6](https://arxiv.org/html/2605.23054v1#S6.SS0.SSS0.Px2.p1.1 "Engagement with linguistic theory. ‣ 6 Discussion ‣ Model Collapse as Cultural Evolution").

- Galke et al. (2023)L. Galke, Y. Ram, and L. RavivWhat makes a language easy to deep-learn? deep neural networks and humans similarly benefit from compositional structure.
arXiv preprintarXiv.2302.12239.
External Links: [Link](https://doi.org/10.48550/arXiv.2302.12239 ""),
[Document](https://dx.doi.org/10.48550/ARXIV.2302.12239 ""),
2302.12239Cited by: [§1](https://arxiv.org/html/2605.23054v1#S1.p3.1 "1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px2.p1.1 "Cultural evolution and LLMs. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution").

- Galke et al. (2024)L. Galke, Y. Ram, and L. RavivDeep neural networks and humans both benefit from compositional language structure.
Nature Communications15 (1).
External Links: ISSN 2041-1723,
[Document](https://dx.doi.org/10.1038/s41467-024-55158-1 "")Cited by: [§3.4](https://arxiv.org/html/2605.23054v1#S3.SS4.SSS0.Px5.p1.1 "Collapse-robust validation. ‣ 3.4 Linguistic Metrics ‣ 3 Methods ‣ Model Collapse as Cultural Evolution"),
[§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px2.p1.1 "Cultural evolution and LLMs. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution").

- Gerstgrasser et al. (2024)M. Gerstgrasser, R. Schaeffer, A. Dey, R. Rafailov, T. Korbak, H. Sleight, R. Agrawal, J. Hughes, D. B. Pai, A. Gromov, D. Roberts, D. Yang, D. L. Donoho, and S. KoyejoIs model collapse inevitable? breaking the curse of recursion by accumulating real and synthetic data.
In First Conference on Language Modeling,
External Links: [Link](https://openreview.net/forum?id=5B2K4LRgmz "")Cited by: [§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px1.p1.1 "Model collapse. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution"),
[§6](https://arxiv.org/html/2605.23054v1#S6.SS0.SSS0.Px3.p1.1 "Implications and reconciliation of concurrent results. ‣ 6 Discussion ‣ Model Collapse as Cultural Evolution").

- Gillman et al. (2024)N. Gillman, M. Freeman, D. Aggarwal, C. Hsu, C. Luo, Y. Tian, and C. SunSelf-correcting self-consuming loops for generative model training.
In Forty-first International Conference on Machine Learning, ICML 2024,
Vienna, Austria, July 21-27, 2024, R. Salakhutdinov, Z. Kolter, K. A. Heller, A. Weller, N. Oliver, J. Scarlett, and F. Berkenkamp (Eds.),
Proceedings of Machine Learning Research, Vol. 235, pp. 15646–15677.
Cited by: [§3.3](https://arxiv.org/html/2605.23054v1#S3.SS3.p2.1 "3.3 Three-Condition Filtering Experiment ‣ 3 Methods ‣ Model Collapse as Cultural Evolution").

- Goldberg (2005)A. GoldbergConstructions at work: the nature of generalization in language.
Oxford University PressOxford.
External Links: ISBN 9780191708428,
[Document](https://dx.doi.org/10.1093/acprof%3Aoso/9780199268511.001.0001 "")Cited by: [Appendix N](https://arxiv.org/html/2605.23054v1#A14.p1.1 "Appendix N CxG Entrenchment Analysis Details ‣ Model Collapse as Cultural Evolution"),
[Appendix V](https://arxiv.org/html/2605.23054v1#A22.p2.1 "Appendix V Discussion: Construction Grammar and Human Parallels ‣ Model Collapse as Cultural Evolution"),
[§3.4](https://arxiv.org/html/2605.23054v1#S3.SS4.SSS0.Px3.p1.1 "Construction diversity (𝒟). ‣ 3.4 Linguistic Metrics ‣ 3 Methods ‣ Model Collapse as Cultural Evolution"),
[§4.3](https://arxiv.org/html/2605.23054v1#S4.SS3.p2.1 "4.3 P3 (Partially Discriminative): Dimension-Specific Degradation Rates ‣ 4 Results ‣ Model Collapse as Cultural Evolution"),
[§6](https://arxiv.org/html/2605.23054v1#S6.SS0.SSS0.Px2.p1.1 "Engagement with linguistic theory. ‣ 6 Discussion ‣ Model Collapse as Cultural Evolution").

- Griffiths and Kalish (2007)T. L. Griffiths and M. L. KalishLanguage evolution by iterated learning with bayesian agents.
Cogn. Sci.31 (3), pp. 441–480.
External Links: [Document](https://dx.doi.org/10.1080/15326900701326576 "")Cited by: [Appendix L](https://arxiv.org/html/2605.23054v1#A12.p1.1 "Appendix L Convergence and Attractor Characterization ‣ Model Collapse as Cultural Evolution"),
[§1](https://arxiv.org/html/2605.23054v1#S1.p1.1 "1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§2.1](https://arxiv.org/html/2605.23054v1#S2.SS1.p1.1 "2.1 Iterated Learning and the Compression–Communication Tradeoff ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution"),
[§2.2](https://arxiv.org/html/2605.23054v1#S2.SS2.p2.1 "2.2 LLM Self-Training as Iterated Learning ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution"),
[Figure 1](https://arxiv.org/html/2605.23054v1#S3.F1 "In 3.1 Self-Training Pipeline ‣ 3 Methods ‣ Model Collapse as Cultural Evolution"),
[§3.1](https://arxiv.org/html/2605.23054v1#S3.SS1.SSS0.Px2.p1.1 "Generations 1–10. ‣ 3.1 Self-Training Pipeline ‣ 3 Methods ‣ Model Collapse as Cultural Evolution"),
[§4.1](https://arxiv.org/html/2605.23054v1#S4.SS1.SSS0.Px2.p1.1 "Regularized-seed control. ‣ 4.1 P4 (Critical Discriminative Test): The Compression–Communication Tradeoff ‣ 4 Results ‣ Model Collapse as Cultural Evolution"),
[§4.5](https://arxiv.org/html/2605.23054v1#S4.SS5.p2.1 "4.5 Sensitivity Analyses: Temperature and Cross-Model ‣ 4 Results ‣ Model Collapse as Cultural Evolution").

- Guo et al. (2024)Y. Guo, G. Shang, M. Vazirgiannis, and C. ClavelThe curious decline of linguistic diversity: training language models on synthetic text.
In Findings of the Association for Computational Linguistics: NAACL 2024, K. Duh, H. Gomez, and S. Bethard (Eds.),
Mexico City, Mexico, pp. 3589–3604.
External Links: [Link](https://aclanthology.org/2024.findings-naacl.228/ ""),
[Document](https://dx.doi.org/10.18653/v1/2024.findings-naacl.228 "")Cited by: [§1](https://arxiv.org/html/2605.23054v1#S1.p2.1 "1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px1.p1.1 "Model collapse. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution").

- Gutierrez-Vasques and Mijangos (2020)X. Gutierrez-Vasques and V. MijangosProductivity and predictability for measuring morphological complexity.
Entropy22 (1).
External Links: [Document](https://dx.doi.org/10.3390/e22010048 "")Cited by: [Appendix R](https://arxiv.org/html/2605.23054v1#A18.p1.1 "Appendix R Cross-Linguistic Morphology Details ‣ Model Collapse as Cultural Evolution"),
[§3.4](https://arxiv.org/html/2605.23054v1#S3.SS4.SSS0.Px2.p1.1 "Morphological regularity (𝜌_𝑀). ‣ 3.4 Linguistic Metrics ‣ 3 Methods ‣ Model Collapse as Cultural Evolution"),
[§3.5](https://arxiv.org/html/2605.23054v1#S3.SS5.p1.1 "3.5 Human Baselines and Cross-Linguistic Extension ‣ 3 Methods ‣ Model Collapse as Cultural Evolution").

- Hedges (1981)L. V. HedgesDistribution theory for glass’s estimator of effect size and related estimators.
Journal of Educational Statistics6 (2), pp. 107.
External Links: ISSN 0362-9791,
[Document](https://dx.doi.org/10.2307/1164588 "")Cited by: [§4](https://arxiv.org/html/2605.23054v1#S4.p1.1 "4 Results ‣ Model Collapse as Cultural Evolution").

- Hesterberg (2015)T. C. HesterbergWhat teachers should know about the bootstrap: resampling in the undergraduate statistics curriculum.
The American Statistician69 (4), pp. 371–386.
External Links: ISSN 1537-2731,
[Document](https://dx.doi.org/10.1080/00031305.2015.1089789 "")Cited by: [§4](https://arxiv.org/html/2605.23054v1#S4.p1.1 "4 Results ‣ Model Collapse as Cultural Evolution").

- Holtzman et al. (2020)A. Holtzman, J. Buys, L. Du, M. Forbes, and Y. ChoiThe curious case of neural text degeneration.
In 8th International Conference on Learning Representations, ICLR 2020,
Addis Ababa, Ethiopia, April 26-30, 2020,
Cited by: [Appendix W](https://arxiv.org/html/2605.23054v1#A23.SS0.SSS0.Px1.p1.1 "Compositionality and inductive biases. ‣ Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution").

- Hudson Kam and Newport (2005)C. L. Hudson Kam and E. L. NewportRegularizing unpredictable variation: the roles of adult and child learners in language formation and change.
Language Learning and Development1 (2), pp. 151–195.
External Links: ISSN 1547-3341,
[Document](https://dx.doi.org/10.1080/15475441.2005.9684215 "")Cited by: [Appendix V](https://arxiv.org/html/2605.23054v1#A22.p1.1 "Appendix V Discussion: Construction Grammar and Human Parallels ‣ Model Collapse as Cultural Evolution"),
[§2.2](https://arxiv.org/html/2605.23054v1#S2.SS2.p4.1 "2.2 LLM Self-Training as Iterated Learning ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution").

- Hudson Kam and Newport (2009)C. L. Hudson Kam and E. L. NewportGetting it right by getting it wrong: when learners change languages.
Cognitive Psychology59 (1), pp. 30–66.
External Links: ISSN 0010-0285,
[Document](https://dx.doi.org/10.1016/j.cogpsych.2009.01.001 "")Cited by: [Appendix V](https://arxiv.org/html/2605.23054v1#A22.p1.1 "Appendix V Discussion: Construction Grammar and Human Parallels ‣ Model Collapse as Cultural Evolution"),
[§2.2](https://arxiv.org/html/2605.23054v1#S2.SS2.p4.1 "2.2 LLM Self-Training as Iterated Learning ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution").

- Hupkes et al. (2020)D. Hupkes, V. Dankers, M. Mul, and E. BruniCompositionality decomposed: how do neural networks generalise?.
J. Artif. Intell. Res.67, pp. 757–795.
External Links: [Document](https://dx.doi.org/10.1613/JAIR.1.11674 "")Cited by: [Appendix W](https://arxiv.org/html/2605.23054v1#A23.SS0.SSS0.Px1.p1.1 "Compositionality and inductive biases. ‣ Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution").

- Jiang et al. (2023)A. Q. Jiang, A. Sablayrolles, A. Mensch, C. Bamford, D. S. Chaplot, D. d. l. Casas, F. Bressand, G. Lengyel, G. Lample, L. Saulnier, L. R. Lavaud, M. Lachaux, P. Stock, T. L. Scao, T. Lavril, T. Wang, T. Lacroix, and W. E. SayedMistral 7b.
arXiv preprintarXiv.2310.06825.
Note: arXiv preprint arXiv:2310.06825Cited by: [Appendix Q](https://arxiv.org/html/2605.23054v1#A17.p1.1 "Appendix Q Full Mistral-7B Results ‣ Model Collapse as Cultural Evolution"),
[§3.1](https://arxiv.org/html/2605.23054v1#S3.SS1.p1.1 "3.1 Self-Training Pipeline ‣ 3 Methods ‣ Model Collapse as Cultural Evolution").

- Kalish et al. (2007)M. L. Kalish, T. L. Griffiths, and S. LewandowskyIterated learning: intergenerational knowledge transmission reveals inductive biases.
Psychonomic Bulletin & Review14 (2), pp. 288–294.
External Links: ISSN 1531-5320,
[Document](https://dx.doi.org/10.3758/bf03194066 "")Cited by: [Appendix L](https://arxiv.org/html/2605.23054v1#A12.SS0.SSS0.Px1.p1.1 "Attractor characterization. ‣ Appendix L Convergence and Attractor Characterization ‣ Model Collapse as Cultural Evolution"),
[§2.1](https://arxiv.org/html/2605.23054v1#S2.SS1.p1.1 "2.1 Iterated Learning and the Compression–Communication Tradeoff ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution"),
[§3.2](https://arxiv.org/html/2605.23054v1#S3.SS2.p1.1 "3.2 Regularized-Seed Control ‣ 3 Methods ‣ Model Collapse as Cultural Evolution"),
[§4.1](https://arxiv.org/html/2605.23054v1#S4.SS1.SSS0.Px2.p1.1 "Regularized-seed control. ‣ 4.1 P4 (Critical Discriminative Test): The Compression–Communication Tradeoff ‣ 4 Results ‣ Model Collapse as Cultural Evolution").

- Kallini et al. (2024)J. Kallini, I. Papadimitriou, R. Futrell, K. Mahowald, and C. PottsMission: impossible language models.
In Proceedings of the 62nd Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), ACL 2024, Bangkok, Thailand,
August 11-16, 2024, L. Ku, A. Martins, and V. Srikumar (Eds.),
pp. 14691–14714.
External Links: [Document](https://dx.doi.org/10.18653/V1/2024.ACL-LONG.787 "")Cited by: [2nd item](https://arxiv.org/html/2605.23054v1#A19.I1.i2.p1.1 "In Appendix S Bias–Prediction Mapping ‣ Model Collapse as Cultural Evolution"),
[Appendix W](https://arxiv.org/html/2605.23054v1#A23.SS0.SSS0.Px1.p1.1 "Compositionality and inductive biases. ‣ Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution"),
[§1](https://arxiv.org/html/2605.23054v1#S1.SS0.SSS0.Px2.p1.1 "P2: Monotonic regularity increase (confirmatory). ‣ 1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§2.2](https://arxiv.org/html/2605.23054v1#S2.SS2.p3.1 "2.2 LLM Self-Training as Iterated Learning ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution").

- Keysers et al. (2020)D. Keysers, N. Schärli, N. Scales, H. Buisman, D. Furrer, S. Kashubin, N. Momchev, D. Sinopalnikov, L. Stafiniak, T. Tihon, D. Tsarkov, X. Wang, M. van Zee, and O. BousquetMeasuring compositional generalization: a comprehensive method on realistic data.
In 8th International Conference on Learning Representations, ICLR 2020,
Cited by: [Appendix W](https://arxiv.org/html/2605.23054v1#A23.SS0.SSS0.Px1.p1.1 "Compositionality and inductive biases. ‣ Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution").

- Kim and Linzen (2020)N. Kim and T. LinzenCOGS: A compositional generalization challenge based on semantic interpretation.
In Proceedings of the 2020 Conference on Empirical Methods in Natural
Language Processing, EMNLP 2020, Online, November 16-20, 2020, B. Webber, T. Cohn, Y. He, and Y. Liu (Eds.),
pp. 9087–9105.
External Links: [Document](https://dx.doi.org/10.18653/V1/2020.EMNLP-MAIN.731 "")Cited by: [Appendix W](https://arxiv.org/html/2605.23054v1#A23.SS0.SSS0.Px1.p1.1 "Compositionality and inductive biases. ‣ Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution"),
[Appendix D](https://arxiv.org/html/2605.23054v1#A4.p1.1 "Appendix D COGS Evaluation Methodology ‣ Model Collapse as Cultural Evolution"),
[§3.2](https://arxiv.org/html/2605.23054v1#S3.SS2.p1.1 "3.2 Regularized-Seed Control ‣ 3 Methods ‣ Model Collapse as Cultural Evolution"),
[§3.4](https://arxiv.org/html/2605.23054v1#S3.SS4.SSS0.Px4.p1.2 "Compositional systematicity (𝜎). ‣ 3.4 Linguistic Metrics ‣ 3 Methods ‣ Model Collapse as Cultural Evolution").

- Kirby et al. (2008)S. Kirby, H. Cornish, and K. SmithCumulative cultural evolution in the laboratory: an experimental approach to the origins of structure in human language.
Proceedings of the National Academy of Sciences105 (31), pp. 10681–10686.
External Links: [Document](https://dx.doi.org/10.1073/pnas.0707835105 ""),
[Link](https://www.pnas.org/doi/arXiv.10.1073/pnas.0707835105 "")Cited by: [§1](https://arxiv.org/html/2605.23054v1#S1.p1.1 "1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§2.2](https://arxiv.org/html/2605.23054v1#S2.SS2.p4.1 "2.2 LLM Self-Training as Iterated Learning ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution"),
[§3.4](https://arxiv.org/html/2605.23054v1#S3.SS4.SSS0.Px5.p1.1 "Collapse-robust validation. ‣ 3.4 Linguistic Metrics ‣ 3 Methods ‣ Model Collapse as Cultural Evolution").

- Kirby et al. (2014)S. Kirby, T. Griffiths, and K. SmithIterated learning and the evolution of language.
Current Opinion in Neurobiology28, pp. 108–114.
External Links: ISSN 0959-4388,
[Document](https://dx.doi.org/10.1016/j.conb.2014.07.014 "")Cited by: [Appendix J](https://arxiv.org/html/2605.23054v1#A10.p1.1 "Appendix J Bottleneck Width Sensitivity ‣ Model Collapse as Cultural Evolution"),
[Appendix K](https://arxiv.org/html/2605.23054v1#A11.p1.1 "Appendix K Temperature as Bottleneck Severity: Full Results ‣ Model Collapse as Cultural Evolution"),
[§1](https://arxiv.org/html/2605.23054v1#S1.p1.1 "1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§2.1](https://arxiv.org/html/2605.23054v1#S2.SS1.p2.1 "2.1 Iterated Learning and the Compression–Communication Tradeoff ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution"),
[§2.2](https://arxiv.org/html/2605.23054v1#S2.SS2.p4.1 "2.2 LLM Self-Training as Iterated Learning ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution"),
[§4.5](https://arxiv.org/html/2605.23054v1#S4.SS5.p1.1 "4.5 Sensitivity Analyses: Temperature and Cross-Model ‣ 4 Results ‣ Model Collapse as Cultural Evolution").

- Kirby et al. (2015)S. Kirby, M. Tamariz, H. Cornish, and K. SmithCompression and communication in the cultural evolution of linguistic structure.
Cognition141, pp. 87–102.
External Links: ISSN 0010-0277,
[Document](https://dx.doi.org/10.1016/j.cognition.2015.03.016 "")Cited by: [Appendix K](https://arxiv.org/html/2605.23054v1#A11.p2.1 "Appendix K Temperature as Bottleneck Severity: Full Results ‣ Model Collapse as Cultural Evolution"),
[§1](https://arxiv.org/html/2605.23054v1#S1.SS0.SSS0.Px4.p1.1 "P4: Non-monotonic compositionality (uniquely discriminative, critical test). ‣ 1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§1](https://arxiv.org/html/2605.23054v1#S1.p1.1 "1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§2.1](https://arxiv.org/html/2605.23054v1#S2.SS1.p2.1 "2.1 Iterated Learning and the Compression–Communication Tradeoff ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution"),
[§2.3](https://arxiv.org/html/2605.23054v1#S2.SS3.p1.1 "2.3 Predictions and Discriminative Status ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution"),
[§3.3](https://arxiv.org/html/2605.23054v1#S3.SS3.p1.1 "3.3 Three-Condition Filtering Experiment ‣ 3 Methods ‣ Model Collapse as Cultural Evolution"),
[§3.3](https://arxiv.org/html/2605.23054v1#S3.SS3.p2.1 "3.3 Three-Condition Filtering Experiment ‣ 3 Methods ‣ Model Collapse as Cultural Evolution"),
[§4.1](https://arxiv.org/html/2605.23054v1#S4.SS1.SSS0.Px3.p1.1 "Three-condition filtering. ‣ 4.1 P4 (Critical Discriminative Test): The Compression–Communication Tradeoff ‣ 4 Results ‣ Model Collapse as Cultural Evolution"),
[§4](https://arxiv.org/html/2605.23054v1#S4.p1.1 "4 Results ‣ Model Collapse as Cultural Evolution"),
[§6](https://arxiv.org/html/2605.23054v1#S6.SS0.SSS0.Px1.p1.1 "Summary of findings. ‣ 6 Discussion ‣ Model Collapse as Cultural Evolution").

- Kouwenhoven et al. (2025a)T. Kouwenhoven, M. Peeperkorn, R. D. Kleijn, and T. VerhoefShaping shared languages: human and large language models’ inductive biases in emergent communication.
In Proceedings of the Thirty-Fourth International Joint Conference on
Artificial Intelligence, IJCAI 2025, Montreal, Canada, August 16-22,
2025,
pp. 10298–10306.
External Links: [Link](https://doi.org/10.24963/ijcai.2025/1144 ""),
[Document](https://dx.doi.org/10.24963/IJCAI.2025/1144 "")Cited by: [§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px2.p1.1 "Cultural evolution and LLMs. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution"),
[§6](https://arxiv.org/html/2605.23054v1#S6.SS0.SSS0.Px3.p1.1 "Implications and reconciliation of concurrent results. ‣ 6 Discussion ‣ Model Collapse as Cultural Evolution").

- Kouwenhoven et al. (2025b)T. Kouwenhoven, M. Peeperkorn, and T. VerhoefSearching for structure: investigating emergent communication with large language models.
In Proceedings of the 31st International Conference on Computational Linguistics, O. Rambow, L. Wanner, M. Apidianaki, H. Al-Khalifa, B. D. Eugenio, and S. Schockaert (Eds.),
Abu Dhabi, UAE, pp. 9977–9991.
External Links: [Link](https://aclanthology.org/2025.coling-main.667/ "")Cited by: [§1](https://arxiv.org/html/2605.23054v1#S1.p3.1 "1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px2.p1.1 "Cultural evolution and LLMs. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution"),
[§6](https://arxiv.org/html/2605.23054v1#S6.SS0.SSS0.Px3.p1.1 "Implications and reconciliation of concurrent results. ‣ 6 Discussion ‣ Model Collapse as Cultural Evolution").

- Lake and Baroni (2018)B. M. Lake and M. BaroniGeneralization without systematicity: on the compositional skills of sequence-to-sequence recurrent networks.
In Proceedings of the 35th International Conference on Machine Learning,
ICML 2018, Stockholmsmässan, Stockholm, Sweden, July
10-15, 2018, J. G. Dy and A. Krause (Eds.),
Proceedings of Machine Learning Research, Vol. 80, pp. 2879–2888.
External Links: [Link](http://proceedings.mlr.press/v80/lake18a.html "")Cited by: [Appendix W](https://arxiv.org/html/2605.23054v1#A23.SS0.SSS0.Px1.p1.1 "Compositionality and inductive biases. ‣ Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution").

- Lake and Baroni (2023)B. M. Lake and M. BaroniHuman-like systematic generalization through a meta-learning neural network.
Nat.623 (7985), pp. 115–121.
External Links: [Document](https://dx.doi.org/10.1038/S41586-023-06668-3 "")Cited by: [Appendix W](https://arxiv.org/html/2605.23054v1#A23.SS0.SSS0.Px1.p1.1 "Compositionality and inductive biases. ‣ Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution").

- Lakens (2013)D. LakensCalculating and reporting effect sizes to facilitate cumulative science: a practical primer for t-tests and anovas.
Frontiers in Psychology4.
External Links: ISSN 1664-1078,
[Document](https://dx.doi.org/10.3389/fpsyg.2013.00863 "")Cited by: [§4](https://arxiv.org/html/2605.23054v1#S4.p1.1 "4 Results ‣ Model Collapse as Cultural Evolution").

- Lazaridou and Baroni (2020)A. Lazaridou and M. BaroniEmergent multi-agent communication in the deep learning era.
arXiv preprintarXiv.2006.02419.
Cited by: [Appendix W](https://arxiv.org/html/2605.23054v1#A23.SS0.SSS0.Px1.p1.1 "Compositionality and inductive biases. ‣ Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution").

- Lazaridou et al. (2017)A. Lazaridou, A. Peysakhovich, and M. BaroniMulti-agent cooperation and the emergence of (natural) language.
In 5th International Conference on Learning Representations, ICLR 2017,
Toulon, France, April 24-26, 2017, Conference Track Proceedings,
Cited by: [Appendix W](https://arxiv.org/html/2605.23054v1#A23.SS0.SSS0.Px1.p1.1 "Compositionality and inductive biases. ‣ Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution").

- Lupyan and Dale (2010)G. Lupyan and R. DaleLanguage structure is partly determined by social structure.
PLoS ONE5 (1), pp. e8559.
External Links: ISSN 1932-6203,
[Document](https://dx.doi.org/10.1371/journal.pone.0008559 "")Cited by: [§4.4](https://arxiv.org/html/2605.23054v1#S4.SS4.p1.1 "4.4 P2 and P5 (Confirmatory): Regularity Increase and Distributional Narrowing ‣ 4 Results ‣ Model Collapse as Cultural Evolution").

- Mahowald et al. (2023)K. Mahowald, A. A. Ivanova, I. A. Blank, N. Kanwisher, J. B. Tenenbaum, and E. FedorenkoDissociating language and thought in large language models: a cognitive perspective.
arXiv preprintarXiv.2301.06627.
External Links: [Document](https://dx.doi.org/10.48550/ARXIV.2301.06627 "")Cited by: [Appendix V](https://arxiv.org/html/2605.23054v1#A22.p1.1 "Appendix V Discussion: Construction Grammar and Human Parallels ‣ Model Collapse as Cultural Evolution"),
[§1](https://arxiv.org/html/2605.23054v1#S1.SS0.SSS0.Px3.p1.1 "P3: Dimension-specific degradation rates (partially discriminative). ‣ 1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§2.3](https://arxiv.org/html/2605.23054v1#S2.SS3.p1.1 "2.3 Predictions and Discriminative Status ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution"),
[§4.2](https://arxiv.org/html/2605.23054v1#S4.SS2.p3.1 "4.2 P1 (Partially Discriminative): Frequency-Dependent Loss Order with Human Comparison ‣ 4 Results ‣ Model Collapse as Cultural Evolution"),
[§4.3](https://arxiv.org/html/2605.23054v1#S4.SS3.p2.1 "4.3 P3 (Partially Discriminative): Dimension-Specific Degradation Rates ‣ 4 Results ‣ Model Collapse as Cultural Evolution"),
[§6](https://arxiv.org/html/2605.23054v1#S6.SS0.SSS0.Px2.p1.1 "Engagement with linguistic theory. ‣ 6 Discussion ‣ Model Collapse as Cultural Evolution").

- McCoy et al. (2020)R. T. McCoy, R. Frank, and T. LinzenDoes syntax need to grow on trees? sources of hierarchical inductive bias in sequence-to-sequence networks.
Trans. Assoc. Comput. Linguistics8, pp. 125–140.
External Links: [Document](https://dx.doi.org/10.1162/TACL%5FA%5F00304 "")Cited by: [Appendix W](https://arxiv.org/html/2605.23054v1#A23.SS0.SSS0.Px1.p1.1 "Compositionality and inductive biases. ‣ Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution").

- McCoy and Griffiths (2025)R. T. McCoy and T. L. GriffithsModeling rapid language learning by distilling Bayesian priors into artificial neural networks.
Nature Communications16, pp. 4676.
External Links: [Document](https://dx.doi.org/10.1038/s41467-025-59957-y "")Cited by: [Appendix W](https://arxiv.org/html/2605.23054v1#A23.SS0.SSS0.Px1.p1.1 "Compositionality and inductive biases. ‣ Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution"),
[§2.2](https://arxiv.org/html/2605.23054v1#S2.SS2.p4.1 "2.2 LLM Self-Training as Iterated Learning ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution").

- McCoy et al. (2024)R. T. McCoy, S. Yao, D. Friedman, M. D. Hardy, and T. L. GriffithsEmbers of autoregression show how large language models are shaped by the problem they are trained to solve.
Proceedings of the National Academy of Sciences121 (41).
External Links: ISSN 1091-6490,
[Document](https://dx.doi.org/10.1073/pnas.2322420121 "")Cited by: [3rd item](https://arxiv.org/html/2605.23054v1#A19.I1.i3.p1.1 "In Appendix S Bias–Prediction Mapping ‣ Model Collapse as Cultural Evolution"),
[Appendix W](https://arxiv.org/html/2605.23054v1#A23.SS0.SSS0.Px1.p1.1 "Compositionality and inductive biases. ‣ Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution"),
[§2.2](https://arxiv.org/html/2605.23054v1#S2.SS2.p3.1 "2.2 LLM Self-Training as Iterated Learning ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution").

- Meister et al. (2023)C. Meister, T. Pimentel, G. Wiher, and R. CotterellLocally typical sampling.
Transactions of the Association for Computational Linguistics11, pp. 102–121.
External Links: ISSN 2307-387X,
[Document](https://dx.doi.org/10.1162/tacl%5Fa%5F00536 "")Cited by: [Appendix W](https://arxiv.org/html/2605.23054v1#A23.SS0.SSS0.Px1.p1.1 "Compositionality and inductive biases. ‣ Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution").

- Misra and Mahowald (2024)K. Misra and K. MahowaldLanguage models learn rare phenomena from less rare phenomena: the case of the missing aanns.
arXiv preprintarXiv.2403.19827.
Cited by: [Appendix V](https://arxiv.org/html/2605.23054v1#A22.p2.1 "Appendix V Discussion: Construction Grammar and Human Parallels ‣ Model Collapse as Cultural Evolution"),
[Appendix W](https://arxiv.org/html/2605.23054v1#A23.SS0.SSS0.Px1.p1.1 "Compositionality and inductive biases. ‣ Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution").

- Morgan and Levy (2016)E. Morgan and R. LevyFrequency-dependent regularization in iterated learning.
In The Evolution of Language: Proceedings of the 11th International Conference (EVOLANG11), S. G. Roberts, C. Cuskley, L. McCrohon, L. Barceló-Coblijn, O. Fehér, and T. Verhoef (Eds.),
External Links: [Link](http://evolang.org/neworleans/papers/193.html "")Cited by: [Figure 4](https://arxiv.org/html/2605.23054v1#A21.F4 "In Appendix U Human Regularization Overlay ‣ Model Collapse as Cultural Evolution"),
[Appendix V](https://arxiv.org/html/2605.23054v1#A22.p1.1 "Appendix V Discussion: Construction Grammar and Human Parallels ‣ Model Collapse as Cultural Evolution"),
[§1](https://arxiv.org/html/2605.23054v1#S1.SS0.SSS0.Px1.p1.1 "P1: Frequency-dependent loss order (partially discriminative). ‣ 1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§1](https://arxiv.org/html/2605.23054v1#S1.SS0.SSS0.Px5.p2.1 "P5: Distributional narrowing (confirmatory). ‣ 1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§2.3](https://arxiv.org/html/2605.23054v1#S2.SS3.p1.1 "2.3 Predictions and Discriminative Status ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution"),
[§3.5](https://arxiv.org/html/2605.23054v1#S3.SS5.p1.1 "3.5 Human Baselines and Cross-Linguistic Extension ‣ 3 Methods ‣ Model Collapse as Cultural Evolution"),
[§4.2](https://arxiv.org/html/2605.23054v1#S4.SS2.p2.1 "4.2 P1 (Partially Discriminative): Frequency-Dependent Loss Order with Human Comparison ‣ 4 Results ‣ Model Collapse as Cultural Evolution"),
[§6](https://arxiv.org/html/2605.23054v1#S6.SS0.SSS0.Px2.p1.1 "Engagement with linguistic theory. ‣ 6 Discussion ‣ Model Collapse as Cultural Evolution"),
[§7](https://arxiv.org/html/2605.23054v1#S7.p1.1 "7 Limitations ‣ Model Collapse as Cultural Evolution").

- Mu and Goodman (2021)J. Mu and N. D. GoodmanEmergent communication of generalizations.
In Advances in Neural Information Processing Systems 34: Annual Conference
on Neural Information Processing Systems 2021, NeurIPS 2021, December
6-14, 2021, virtual, M. Ranzato, A. Beygelzimer, Y. N. Dauphin, P. Liang, and J. W. Vaughan (Eds.),
pp. 17994–18007.
Cited by: [Appendix W](https://arxiv.org/html/2605.23054v1#A23.SS0.SSS0.Px1.p1.1 "Compositionality and inductive biases. ‣ Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution").

- Nikolaus et al. (2021)M. Nikolaus, J. Maes, and A. FourtassiModeling speech act development in early childhood: The role of frequency and linguistic cues.
In Proceedings of the 43rd Annual Meeting of the Cognitive Science Society,
External Links: [Link](https://escholarship.org/uc/item/10k7j8fr "")Cited by: [Appendix W](https://arxiv.org/html/2605.23054v1#A23.SS0.SSS0.Px1.p1.1 "Compositionality and inductive biases. ‣ Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution").

- Perez et al. (2024)J. Perez, C. Léger, M. Ovando-Tellez, C. Foulon, J. Dussauld, P. Oudeyer, and C. Moulin-FrierCultural evolution in populations of large language models.
Vol. arXiv.2403.08882.
Cited by: [§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px2.p1.1 "Cultural evolution and LLMs. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution").

- Piantadosi (2014)S. T. PiantadosiZipf’s word frequency law in natural language: a critical review and future directions.
Psychonomic Bulletin & Review21 (5), pp. 1112–1130.
External Links: ISSN 1531-5320,
[Document](https://dx.doi.org/10.3758/s13423-014-0585-6 "")Cited by: [§1](https://arxiv.org/html/2605.23054v1#S1.SS0.SSS0.Px5.p1.1 "P5: Distributional narrowing (confirmatory). ‣ 1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§3.4](https://arxiv.org/html/2605.23054v1#S3.SS4.SSS0.Px1.p1.1 "Zipf exponent (𝛼). ‣ 3.4 Linguistic Metrics ‣ 3 Methods ‣ Model Collapse as Cultural Evolution").

- Raviv et al. (2019)L. Raviv, A. Meyer, and S. Lev-AriLarger communities create more systematic languages.
Proceedings of the Royal Society B: Biological Sciences286 (1907), pp. 20191262.
External Links: ISSN 1471-2954,
[Document](https://dx.doi.org/10.1098/rspb.2019.1262 "")Cited by: [§6](https://arxiv.org/html/2605.23054v1#S6.SS0.SSS0.Px3.p1.1 "Implications and reconciliation of concurrent results. ‣ 6 Discussion ‣ Model Collapse as Cultural Evolution").

- Reali and Griffiths (2009)F. Reali and T. L. GriffithsThe evolution of frequency distributions: relating regularization to inductive biases through iterated learning.
Cognition111 (3), pp. 317–328.
External Links: ISSN 0010-0277,
[Document](https://dx.doi.org/https%3A//doi.org/10.1016/j.cognition.2009.02.012 ""),
[Link](https://www.sciencedirect.com/science/article/pii/S0010027709000432 "")Cited by: [§1](https://arxiv.org/html/2605.23054v1#S1.SS0.SSS0.Px1.p1.1 "P1: Frequency-dependent loss order (partially discriminative). ‣ 1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§2.1](https://arxiv.org/html/2605.23054v1#S2.SS1.p1.1 "2.1 Iterated Learning and the Compression–Communication Tradeoff ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution"),
[§3.5](https://arxiv.org/html/2605.23054v1#S3.SS5.p1.1 "3.5 Human Baselines and Cross-Linguistic Extension ‣ 3 Methods ‣ Model Collapse as Cultural Evolution"),
[§4.2](https://arxiv.org/html/2605.23054v1#S4.SS2.p2.1 "4.2 P1 (Partially Discriminative): Frequency-Dependent Loss Order with Human Comparison ‣ 4 Results ‣ Model Collapse as Cultural Evolution"),
[§7](https://arxiv.org/html/2605.23054v1#S7.p1.1 "7 Limitations ‣ Model Collapse as Cultural Evolution").

- Ren et al. (2020)Y. Ren, S. Guo, M. Labeau, S. B. Cohen, and S. KirbyCompositional languages emerge in a neural iterated learning model.
In 8th International Conference on Learning Representations, ICLR 2020,
Addis Ababa, Ethiopia, April 26-30, 2020,
Cited by: [Appendix W](https://arxiv.org/html/2605.23054v1#A23.SS0.SSS0.Px1.p1.1 "Compositionality and inductive biases. ‣ Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution"),
[§4.1](https://arxiv.org/html/2605.23054v1#S4.SS1.SSS0.Px4.p2.1 "Collapse-robust validation. ‣ 4.1 P4 (Critical Discriminative Test): The Compression–Communication Tradeoff ‣ 4 Results ‣ Model Collapse as Cultural Evolution"),
[§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px2.p1.1 "Cultural evolution and LLMs. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution").

- Ren et al. (2024)Y. Ren, S. Guo, L. Qiu, B. Wang, and D. J. SutherlandBias amplification in language model evolution: an iterated learning perspective.
In Advances in Neural Information Processing Systems 38: Annual Conference
on Neural Information Processing Systems 2024, NeurIPS 2024, Vancouver,
BC, Canada, December 10 - 15, 2024, A. Globersons, L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. M. Tomczak, and C. Zhang (Eds.),
Cited by: [§1](https://arxiv.org/html/2605.23054v1#S1.SS0.SSS0.Px5.p3.1 "P5: Distributional narrowing (confirmatory). ‣ 1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§1](https://arxiv.org/html/2605.23054v1#S1.p3.1 "1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§2.2](https://arxiv.org/html/2605.23054v1#S2.SS2.p2.1 "2.2 LLM Self-Training as Iterated Learning ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution"),
[§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px2.p1.1 "Cultural evolution and LLMs. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution"),
[§6](https://arxiv.org/html/2605.23054v1#S6.SS0.SSS0.Px2.p1.1 "Engagement with linguistic theory. ‣ 6 Discussion ‣ Model Collapse as Cultural Evolution").

- Roy and Vetterli (2007)O. Roy and M. VetterliThe effective rank: A measure of effective dimensionality.
In 15th European Signal Processing Conference, EUSIPCO 2007, Poznan,
Poland, September 3-7, 2007,
pp. 606–610.
Cited by: [§3.4](https://arxiv.org/html/2605.23054v1#S3.SS4.SSS0.Px5.p1.1 "Collapse-robust validation. ‣ 3.4 Linguistic Metrics ‣ 3 Methods ‣ Model Collapse as Cultural Evolution").

- Schaeffer et al. (2025)R. Schaeffer, J. Kazdan, A. C. Arulandu, and S. KoyejoPosition: model collapse does not mean what you think.
arXiv preprintarXiv.2503.03150.
External Links: [Link](https://doi.org/10.48550/arXiv.2503.03150 ""),
[Document](https://dx.doi.org/10.48550/ARXIV.2503.03150 "")Cited by: [§2.2](https://arxiv.org/html/2605.23054v1#S2.SS2.p4.1 "2.2 LLM Self-Training as Iterated Learning ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution"),
[§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px1.p1.1 "Model collapse. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution").

- Seddik et al. (2024)M. E. A. Seddik, S. Chen, S. Hayou, P. Youssef, and M. DebbahHow bad is training on synthetic data? A statistical analysis of language model collapse.
arXiv preprintarXiv.2404.05090.
External Links: [Document](https://dx.doi.org/10.48550/ARXIV.2404.05090 "")Cited by: [§1](https://arxiv.org/html/2605.23054v1#S1.p2.1 "1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px1.p1.1 "Model collapse. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution").

- Shah et al. (2020)H. Shah, K. Tamuly, A. Raghunathan, P. Jain, and P. NetrapalliThe pitfalls of simplicity bias in neural networks.
In Advances in Neural Information Processing Systems 33: Annual Conference
on Neural Information Processing Systems 2020, NeurIPS 2020, December
6-12, 2020, virtual, H. Larochelle, M. Ranzato, R. Hadsell, M. Balcan, and H. Lin (Eds.),
Cited by: [2nd item](https://arxiv.org/html/2605.23054v1#A19.I1.i2.p1.1 "In Appendix S Bias–Prediction Mapping ‣ Model Collapse as Cultural Evolution"),
[§1](https://arxiv.org/html/2605.23054v1#S1.SS0.SSS0.Px2.p1.1 "P2: Monotonic regularity increase (confirmatory). ‣ 1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§2.2](https://arxiv.org/html/2605.23054v1#S2.SS2.p3.1 "2.2 LLM Self-Training as Iterated Learning ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution").

- Shain et al. (2024)C. Shain, C. Meister, T. Pimentel, R. Cotterell, and R. LevyLarge-scale evidence for logarithmic effects of word predictability on reading time.
Proceedings of the National Academy of Sciences121 (10), pp. e2307876121.
External Links: [Document](https://dx.doi.org/10.1073/pnas.2307876121 "")Cited by: [Appendix W](https://arxiv.org/html/2605.23054v1#A23.SS0.SSS0.Px1.p1.1 "Compositionality and inductive biases. ‣ Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution").

- Shumailov et al. (2024)I. Shumailov, Z. Shumaylov, Y. Zhao, N. Papernot, R. Anderson, and Y. GalAI models collapse when trained on recursively generated data.
Nature631.
External Links: [Document](https://dx.doi.org/10.1038/s41586-024-07566-y ""),
ISSN 14764687Cited by: [§1](https://arxiv.org/html/2605.23054v1#S1.p2.1 "1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§1](https://arxiv.org/html/2605.23054v1#S1.p3.1 "1 Introduction ‣ Model Collapse as Cultural Evolution"),
[§2.2](https://arxiv.org/html/2605.23054v1#S2.SS2.p4.1 "2.2 LLM Self-Training as Iterated Learning ‣ 2 Theoretical Framework ‣ Model Collapse as Cultural Evolution"),
[§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px1.p1.1 "Model collapse. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution"),
[§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px2.p1.1 "Cultural evolution and LLMs. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution").

- Taori and Hashimoto (2023)R. Taori and T. HashimotoData feedback loops: model-driven amplification of dataset biases.
In International Conference on Machine Learning, ICML 2023, 23-29 July
2023, Honolulu, Hawaii, USA, A. Krause, E. Brunskill, K. Cho, B. Engelhardt, S. Sabato, and J. Scarlett (Eds.),
Proceedings of Machine Learning Research, Vol. 202, pp. 33883–33920.
Cited by: [§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px1.p1.1 "Model collapse. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution").

- Touvron et al. (2023)H. Touvron, T. Lavril, G. Izacard, X. Martinet, M. Lachaux, T. Lacroix, B. Rozière, N. Goyal, E. Hambro, F. Azhar, A. Rodriguez, A. Joulin, E. Grave, and G. LampleLLaMA: open and efficient foundation language models.
arXiv preprintarXiv.2302.13971.
External Links: [Document](https://dx.doi.org/10.48550/ARXIV.2302.13971 "")Cited by: [§3.1](https://arxiv.org/html/2605.23054v1#S3.SS1.p1.1 "3.1 Self-Training Pipeline ‣ 3 Methods ‣ Model Collapse as Cultural Evolution").

- Warstadt and Bowman (2022)A. Warstadt and S. R. BowmanWhat artificial neural networks can tell us about human language acquisition.
Algebraic structures in natural language, pp. 17–60.
Cited by: [Appendix V](https://arxiv.org/html/2605.23054v1#A22.p1.1 "Appendix V Discussion: Construction Grammar and Human Parallels ‣ Model Collapse as Cultural Evolution"),
[Appendix W](https://arxiv.org/html/2605.23054v1#A23.SS0.SSS0.Px1.p1.1 "Compositionality and inductive biases. ‣ Appendix W Extended Related Work ‣ Model Collapse as Cultural Evolution").

- Weissweiler et al. (2024)L. Weissweiler, N. Böbel, K. Guiller, S. Herrera, W. Scivetti, A. Lorenzi, N. Melnik, A. Bhatia, H. Schütze, L. Levin, A. Zeldes, J. Nivre, W. Croft, and N. SchneiderUCxn: typologically informed annotation of constructions atop Universal Dependencies.
In Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024), N. Calzolari, M. Kan, V. Hoste, A. Lenci, S. Sakti, and N. Xue (Eds.),
Torino, Italia, pp. 16919–16932.
External Links: [Link](https://aclanthology.org/2024.lrec-main.1471/ "")Cited by: [§3.5](https://arxiv.org/html/2605.23054v1#S3.SS5.p1.1 "3.5 Human Baselines and Cross-Linguistic Extension ‣ 3 Methods ‣ Model Collapse as Cultural Evolution"),
[§7](https://arxiv.org/html/2605.23054v1#S7.p1.1 "7 Limitations ‣ Model Collapse as Cultural Evolution").

- Zheng et al. (2024)C. Zheng, J. Zhang, A. Kembhavi, and R. KrishnaIterated learning improves compositionality in large vision-language models.
In IEEE/CVF Conference on Computer Vision and Pattern Recognition,
CVPR 2024, Seattle, WA, USA, June 16-22, 2024,
pp. 13785–13795.
External Links: [Document](https://dx.doi.org/10.1109/CVPR52733.2024.01308 "")Cited by: [§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px2.p1.1 "Cultural evolution and LLMs. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution").

- Zhu and Griffiths (2024)J. Zhu and T. L. GriffithsEliciting the priors of large language models using iterated in-context learning.
arXiv preprintarXiv.2406.01860.
External Links: [Link](https://arxiv.org/arXiv.2406.01860 "")Cited by: [§5](https://arxiv.org/html/2605.23054v1#S5.SS0.SSS0.Px2.p1.1 "Cultural evolution and LLMs. ‣ 5 Related Work ‣ Model Collapse as Cultural Evolution").


## Appendix A Construction Inventory

The 50 construction types span five syntactic categories: argument structure constructions (simple transitive, ditransitive, caused-motion, resultative, way-construction), clause types (declarative, interrogative, imperative, exclamative, relative clause), information structure (topicalization, left-dislocation, cleft, pseudo-cleft, existential), complex predicates (serial verb, light verb, particle verb, phrasal verb), and discourse-level constructions (quotative inversion, comparative correlative, rhetorical question). Each is identified via dependency parse patterns using spaCy’s en\_core\_web\_trf model. Full pattern specifications are available in the released code.

## Appendix B Construction Identification Reliability

| Quartile | Precision | Recall | F1 |
| --- | --- | --- | --- |
| Q4 (frequent) | 0.94 | 0.96 | 0.95 |
| Q3 | 0.91 | 0.93 | 0.92 |
| Q2 | 0.87 | 0.88 | 0.87 |
| Q1 (rare) | 0.82 | 0.84 | 0.83 |

Table 3: SpaCy construction identification accuracy by quartile (manual validation on late-generation text).

While Q1 precision is lower (0.82 vs. 0.94 for Q4), this 12-point gap cannot account for the 56-point gap in entropy retention (32% vs. 88%). Even assuming all Q1 parser errors are false negatives (overestimating loss), corrected Q1 retention would be ≈\\approx39%, still substantially below Q4.

## Appendix C TopSim Diagnostic Dashboard

| Gen. | σ\\sigma | eRM | eRF | posdis | zMantelz\_{\\text{Mantel}} | #Uniq |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.41 | 12.4 | 9.8 | 0.31 | 4.2 | 847 |
| 1 | 0.43 | 12.3 | 9.5 | 0.33 | 4.5 | 821 |
| 3 | 0.47 | 12.1 | 9.2 | 0.36 | 5.1 | 764 |
| 5 | 0.44 | 11.4 | 8.3 | 0.33 | 4.7 | 682 |
| 7 | 0.38 | 9.8 | 6.7 | 0.27 | 4.1 | 531 |
| 10 | 0.31 | 7.2 | 4.8 | 0.22 | 3.8 | 394 |

Table 4: Collapse-robust compositionality diagnostics (LLaMA-2, unfiltered). eRM and eRF: effective rank for meaning and form spaces. During the compositionality rise (Gen. 0–3), eRM remains stable (12.4→\\to12.1) while σ\\sigma increases, confirming genuine systematicity. All Mantel zz-scores exceed the permutation null (z>3.8z>3.8, p<0.001p<0.001).

The diagnostic pattern is clear: during generations 0–3, σ\\sigma increases while meaning-space eRank remains essentially stable, confirming the initial rise reflects a genuine increase in the systematicity of the form–meaning mapping rather than dual-space collapse. Posdis shows the same non-monotonic trajectory as σ\\sigma, providing convergent evidence from a metric that excludes collapsed positions by construction ( [Chaabouni et al., 2020](https://arxiv.org/html/2605.23054v1#bib.bib13 "")).

## Appendix D COGS Evaluation Methodology

COGS ( [Kim and Linzen, 2020](https://arxiv.org/html/2605.23054v1#bib.bib19 "")) evaluates compositional generalization via novel sentence-to-logical-form mappings. We evaluate via _5-shot prompting_: each generation’s model receives COGS test sentences with 5 in-context examples of the sentence-to-logical-form mapping, without additional fine-tuning on COGS training data, to avoid confounding compositionality loss with domain shift. Accuracy is measured as exact match to the gold logical form. This 5-shot approach measures the model’s existing compositional capacity.

## Appendix E Regularized-Seed Experiment Details

The regularized seed corpus is generated from a PCFG with the following properties: (i) 12 verb frames with consistent argument structure (every transitive verb takes NP-V-NP; every ditransitive takes NP-V-NP-PP); (ii) regular morphology (all past tenses formed by _-ed_ suffixation); (iii) systematic form–meaning mappings (each semantic role is expressed by a fixed syntactic position). The grammar produces passages of 100–300 tokens with vocabulary size matching the natural seed (≈\\approx28,000 types). Generation-by-generation results are reported in Figure [2](https://arxiv.org/html/2605.23054v1#S4.F2 "Figure 2 ‣ 4.1 P4 (Critical Discriminative Test): The Compression–Communication Tradeoff ‣ 4 Results ‣ Model Collapse as Cultural Evolution") (orange dashed line).

## Appendix F Three-Condition Filtering Full Results

| Gen. 10 metric | No filter | Random | Quality |
| --- | --- | --- | --- |
| σ\\sigma | 0.31 | 0.33 | 0.48 |
| COGS | 0.21 | 0.23 | 0.41 |
| α\\alpha | 0.82 | 0.84 | 0.97 |
| ρM\\rho\_{M} | 0.87 | 0.86 | 0.71 |
| 𝒟\\mathcal{D} (bits) | 3.14 | 3.21 | 4.28 |

Table 5: Generation 10 metrics across three filter conditions (LLaMA-2). Random filtering is indistinguishable from no filtering for compositionality (p=0.72p=0.72); only quality filtering sustains compositionality (p<0.001p<0.001).

#### Per-generation trajectories.

The three conditions diverge starting at generation 3. At generation 3, no-filter σ=0.47\\sigma=0.47, random σ=0.47\\sigma=0.47, quality σ=0.49\\sigma=0.49 (the difference is not yet significant). By generation 5, the quality filter trajectory separates clearly: no-filter σ=0.44\\sigma=0.44, random σ=0.44\\sigma=0.44, quality σ=0.51\\sigma=0.51 (p<0.01p<0.01 vs. both other conditions). The divergence increases monotonically through generation 10. This pattern precisely matches the iterated learning prediction that communicative pressure operates cumulatively, with its effect becoming stronger as generations accumulate.

#### Pairwise comparisons.

Using Benjamini–Hochberg FDR correction at q<0.05q<0.05: no-filter vs. random is non-significant for all five metrics (p>0.30p>0.30); quality vs. no-filter is significant for σ\\sigma (p<0.001p<0.001), COGS (p<0.001p<0.001), α\\alpha (p<0.001p<0.001), ρM\\rho\_{M} (p<0.001p<0.001), and 𝒟\\mathcal{D} (p<0.001p<0.001). Quality vs. random shows the same pattern, confirming that the quality filter effect is not attributable to data volume reduction (since random filtering removes the same proportion of data).

## Appendix G Evaluator Independence Analysis

To address concerns about evaluator bias from using the same model family, we replicate the quality filter condition using Flan-T5-XL ( [Chung et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib30 "")) as an alternative evaluator. The compositionality trajectory under Flan-T5-XL evaluation (σ=0.47\\sigma=0.47 at generation 10) is qualitatively identical to the LLaMA-2-13B evaluator (σ=0.48\\sigma=0.48), confirming that compositionality preservation reflects genuine communicative utility rather than distributional mimicry. The correlation between Flan-T5-XL evaluator score and distributional similarity to evaluator outputs is r=0.11r=0.11 (not significant), lower than the r=0.23r=0.23 observed with LLaMA-2-13B, further supporting evaluator independence.

## Appendix H Bayesian Statistical Analysis

Effect sizes, confidence intervals, and Bayesian inference for all key comparisons:

| Prediction | gg | Boot-tt 95% CI | Bayes HDI | BF10\\text{BF}\_{10} |
| --- | --- | --- | --- | --- |
| P1 (Q1 vs. Q4) | 3.08 | \[2.07, 4.09\] | \[1.89, 4.33\] | >>1000 |
| P2 (EN ρM\\rho\_{M}) | 4.27 | \[2.89, 5.65\] | \[2.72, 5.91\] | >>1000 |
| P3 (CxG rr) | 2.11 | \[1.42, 2.80\] | \[1.31, 2.95\] | >>1000 |
| P4 (σ\\sigma peak) | 1.87 | \[1.21, 2.53\] | \[1.09, 2.71\] | 247 |
| P4 (QF vs. NF) | 2.94 | \[1.97, 3.91\] | \[1.82, 4.13\] | >>1000 |
| P5 (α\\alpha) | 1.93 | \[1.26, 2.60\] | \[1.14, 2.78\] | 189 |

Table 6: Statistical inference summary. Hedges’ gg with correction J≈0.903J\\approx 0.903. Bootstrap-tt CIs (B=10,000B=10{,}000; coverage ≈\\approx81–83% at n=5n=5). Bayesian HDIs use Cauchy(0, 0.707) prior. All BF10\\text{BF}\_{10} indicate decisive evidence.

## Appendix I Zipf Goodness-of-Fit

Following [Clauset et al. (2009)](https://arxiv.org/html/2605.23054v1#bib.bib11 ""), we compare the power-law fit against lognormal and exponential alternatives using likelihood ratio tests at each generation. The power-law fit is preferred at all generations (Δ\\DeltaAIC >4>4 vs. lognormal; Δ\\DeltaAIC >12>12 vs. exponential), confirming that the frequency distribution retains its power-law character throughout collapse while the exponent decreases.

## Appendix J Bottleneck Width Sensitivity

With 5K passages per generation (a 10×\\times narrower bottleneck), the P4 compositionality peak shifts from generation 3 to generation 1–2, and convergence to the asymptotic state is reached by generation 15 rather than the estimated 25–30 with 50K passages. This parametric relationship between bottleneck width and convergence speed directly parallels [Kirby et al. (2014)](https://arxiv.org/html/2605.23054v1#bib.bib33 "")’s theoretical predictions and provides strong evidence that the underlying mechanism is shared.

## Appendix K Temperature as Bottleneck Severity: Full Results

| Metric (Gen. 10) | τ=0.5\\tau{=}0.5 | τ=0.8\\tau{=}0.8 | τ=1.0\\tau{=}1.0 |
| Zipf α\\alpha | 0.74 | 0.82 | 0.89 |
| Morph. ρM\\rho\_{M} | 0.92 | 0.87 | 0.81 |
| Constr. 𝒟\\mathcal{D} (bits) | 2.61 | 3.14 | 3.52 |
| Compos. σ\\sigma | 0.24 | 0.31 | 0.37 |
| P4 peak gen. | 2 | 3 | 4 |

Table 7: Effect of temperature on Gen. 10 metrics (LLaMA-2, unfiltered). Lower τ\\tau (tighter bottleneck) accelerates all dynamics. The P4 compositionality peak shifts earlier with tighter bottlenecks, as iterated learning theory predicts. All pairwise differences significant (p<0.001p<0.001, FDR-corrected).

In iterated learning, bottleneck severity determines convergence speed ( [Kirby et al., 2014](https://arxiv.org/html/2605.23054v1#bib.bib33 "")). Table [7](https://arxiv.org/html/2605.23054v1#A11.T7 "Table 7 ‣ Appendix K Temperature as Bottleneck Severity: Full Results ‣ Model Collapse as Cultural Evolution") confirms that τ=0.5\\tau=0.5 accelerates collapse across all metrics. Lower temperature reduces sampling diversity, creating a tighter effective bottleneck analogous to smaller population sizes in human cultural evolution experiments. The P4 compositionality peak shifts from generation 4 (τ=1.0\\tau=1.0) to generation 2 (τ=0.5\\tau=0.5), consistent with narrower bottlenecks accelerating convergence to the prior. This parametric sensitivity provides practitioners with a directly controllable parameter for tuning the rate of structural change in self-training pipelines.

The interaction between temperature and filter condition is also informative: at τ=0.5\\tau=0.5 with quality filtering, compositionality is sustained at σ=0.39\\sigma=0.39 (compared to σ=0.48\\sigma=0.48 at τ=0.8\\tau=0.8), indicating that even communicative pressure is partially overwhelmed by extreme bottleneck narrowing, consistent with [Kirby et al. (2015)](https://arxiv.org/html/2605.23054v1#bib.bib34 "")’s prediction that very strong compression pressure can override communicative pressure.

## Appendix L Convergence and Attractor Characterization

The per-generation rate of change Δn=\|mn−mn−1\|\\Delta\_{n}=\|m\_{n}-m\_{n-1}\| decreases monotonically in later generations (7–10), indicating approach to an asymptotic state. Cross-seed JSD decreases from 0.042±0.0080.042\\pm 0.008 (generation 0) to 0.019±0.0050.019\\pm 0.005 (generation 10, unfiltered), confirming convergence toward a common distribution consistent with convergence to a shared “prior” ( [Griffiths and Kalish, 2007](https://arxiv.org/html/2605.23054v1#bib.bib31 "")).

#### Attractor characterization.

The generation-10 attractor state exhibits consistent properties across all five seeds: α∈\[0.80,0.84\]\\alpha\\in\[0.80,0.84\], ρM∈\[0.85,0.89\]\\rho\_{M}\\in\[0.85,0.89\], σ∈\[0.29,0.33\]\\sigma\\in\[0.29,0.33\]. This narrow range confirms convergence to a well-defined attractor rather than divergence to seed-specific endpoints. The attractor profile (dominant SVO word order, regular morphology, reduced construction diversity concentrated in high-frequency types, and sub-Zipfian frequency distributions) can be interpreted as the LLM’s implicit “prior” over natural language, analogous to the regularization bias revealed by iterated learning in laboratory experiments with human participants ( [Kalish et al., 2007](https://arxiv.org/html/2605.23054v1#bib.bib32 "")).

#### Convergence rate estimation.

Fitting an exponential decay model Δn=Δ0⋅e−λ​n\\Delta\_{n}=\\Delta\_{0}\\cdot e^{-\\lambda n} to the per-generation changes yields λ≈0.18\\lambda\\approx 0.18 for LLaMA-2 (unfiltered, τ=0.8\\tau=0.8), predicting that 95% of convergence is achieved by generation 17. With quality filtering, convergence is slower (λ≈0.09\\lambda\\approx 0.09) because the communicative pressure partially counteracts the prior, consistent with iterated learning predictions that communicative pressure sustains diversity at the cost of slower convergence.

## Appendix M Regularization Examples with Syntactic Context

| Form | Context (Gen. 10) |
| --- | --- |
| _wringed_ | “She _wringed_ the cloth and hung it on the line.” |
| _swimmed_ | “The children _swimmed_ across the lake last summer.” |
| _goed_ | “He _goed_ to the store and bought groceries.” |
| _beed_ | “It _beed_ a long time since we last met.” |

Table 8: Regularized forms in syntactically appropriate contexts (94% of cases), confirming productive regularization rather than hallucination.

## Appendix N CxG Entrenchment Analysis Details

The entrenchment ranking for each of the 50 construction types is estimated from type frequency in the seed data, following standard CxG methodology ( [Goldberg, 2005](https://arxiv.org/html/2605.23054v1#bib.bib46 ""); [Bybee, 2010](https://arxiv.org/html/2605.23054v1#bib.bib47 "")). Survival generation is defined as the last generation at which a construction’s normalized entropy exceeds 50% of its seed value.

| Category | Mean surv. | SD |
| --- | --- | --- |
| Syntactic (transitive, copular) | Gen. 8.7 | 1.2 |
| Morphological (passive, comparative) | Gen. 6.1 | 1.8 |
| Pragmatic (cleft, left-dislocation) | Gen. 4.2 | 1.4 |
| Discourse (rhetorical Q, quot. inv.) | Gen. 3.1 | 0.9 |

Table 9: Mean survival generation by construction category. The ordering pragmatic/discourse << morphological << syntactic confirms P3’s dimension-specific prediction.

The Pearson correlation between log\\log-type-frequency and survival generation is r=0.73r=0.73 (p<0.001p<0.001, 95% CI \[0.58,0.84\]\[0.58,0.84\], n=50n=50, t=7.40t=7.40, df =48=48). We verify robustness with Spearman’s ρ=0.69\\rho=0.69 (p<0.001p<0.001), confirming the relationship is not driven by outliers. The five most resilient constructions are: simple transitive (survival: generation 10), copular (10), passive (9), comparative (8), and ditransitive (8). The five most vulnerable are: quotative inversion (2), comparative correlative (3), rhetorical question (3), left-dislocation (4), and cleft (4). This ordering aligns with CxG entrenchment theory: high-type-frequency constructions with broad productivity resist loss, while low-frequency constructions with narrow collocational profiles are vulnerable.

## Appendix O Prediction Discriminability Analysis

| Pred. | Iterated learning predicts | Generic collapse predicts | What our data show | Control result |
| --- | --- | --- | --- | --- |
| P1 | Log-linear gradient matching human data | Tail loss (no shape prediction) | Log-linear match (R2=0.94R^{2}=0.94) | Human overlay confirms |
| P2 | Regularity increase | Simplicity bias amplification | Confirmed (non-discriminative) | Cross-linguistic replication |
| P3 | Pragmatic >> syntactic >> morphological | Uniform degradation | Dimension-specific order confirmed | CxG entrenchment r=0.73r=0.73 |
| P4 | Non-monotonic: rise then fall; QF sustains | Monotonic degradation only | Non-monotonic confirmed | Reg.-seed persists; random filter fails |
| P5 | Distributional narrowing | Tail loss / variance reduction | Confirmed (non-discriminative) | Power-law fit preferred |

Table 10: Full discriminability analysis including control experiment results.

## Appendix P Human Baseline Corpus Details

Human statistics are computed from: BNC (100M words, 50,000 sampled passages); OpenWebText (50,000 matched passages); Wikipedia (English, Jan 2024, 50,000 passages excl. lists/stubs). Human∗ values in all tables are cross-corpus means. Standard deviations: α\\alpha: 0.03; ρM\\rho\_{M}: 0.02; 𝒟\\mathcal{D}: 0.11; σ\\sigma: 0.04.

## Appendix Q Full Mistral-7B Results

Mistral-7B ( [Jiang et al., 2023](https://arxiv.org/html/2605.23054v1#bib.bib58 "")) replicates all qualitative patterns with somewhat slower degradation rates, consistent with its known stronger coherence in generation tasks.

| Gen. | σ\\sigma (NF) | σ\\sigma (QF) | ρM​-EN\\rho\_{M\\text{-EN}} | α\\alpha |
| --- | --- | --- | --- | --- |
| Seed | 0.41 | 0.41 | 0.62 | 1.07 |
| 1 | 0.43 | 0.44 | 0.63 | 1.05 |
| 3 | 0.48 | 0.50 | 0.67 | 1.01 |
| 5 | 0.45 | 0.51 | 0.73 | 0.96 |
| 7 | 0.39 | 0.50 | 0.78 | 0.91 |
| 10 | 0.34 | 0.47 | 0.84 | 0.86 |

Table 11: Mistral-7B key metrics across generations. NF: no filter; QF: quality filter. All qualitative patterns replicate, with slower degradation rates than LLaMA-2.

Regularized-seed control produces a non-monotonic σ\\sigma trajectory with peak at generation 3 (σ=0.53\\sigma=0.53, declining to 0.340.34). Three-condition filtering shows the same pattern: random filter indistinguishable from no filter (p=0.68p=0.68); quality filter sustains compositionality (σ=0.47\\sigma=0.47 at generation 10). The P4 compositionality peak occurs at the same generation (3) as LLaMA-2, suggesting the peak timing is architecture-independent and depends primarily on the bottleneck parameters. Cross-linguistic morphological regularization follows the same trajectory ordering (Turkish >> English >> German) with slightly lower absolute values at each generation. Complete per-generation tables for all metrics and conditions are provided in the released data.

## Appendix R Cross-Linguistic Morphology Details

German experiments use 150 verbs (75 strong, 75 weak) selected to span frequency quartiles. Strong→\\toweak regularization is measured as the proportion of strong verbs producing weak past tense forms ( _buk_ →\\to _\*backte_). Turkish experiments use 120 verbs testing vowel harmony adherence and suffix regularity. UniMorph paradigm tables ( [Gutierrez-Vasques and Mijangos, 2020](https://arxiv.org/html/2605.23054v1#bib.bib76 "")) provide the gold standard.

## Appendix S Bias–Prediction Mapping

Following [Ferdinand et al. (2019)](https://arxiv.org/html/2605.23054v1#bib.bib2 "")’s demonstration that different bias types produce different evolutionary trajectories, we identify four specific bias–prediction mappings:

- •


_Frequency bias_ from next-token prediction training: high-frequency tokens receive more gradient updates, creating an implicit frequency-dependent prior that drives P1 (frequency-dependent loss) and P5 (distributional narrowing).

- •


_Simplicity bias_ from cross-entropy minimization: [Shah et al. (2020)](https://arxiv.org/html/2605.23054v1#bib.bib12 "") and [Kallini et al. (2024)](https://arxiv.org/html/2605.23054v1#bib.bib16 "") showed LLMs favor regular morphological patterns, driving P2 (regularity increase).

- •


_Local coherence bias_ from autoregressive factorization: [McCoy et al. (2024)](https://arxiv.org/html/2605.23054v1#bib.bib54 "") demonstrated that autoregressive training creates biases toward locally predictable sequences, driving P3’s ordering (pragmatic constructions requiring non-local context are lost first).

- •


_Compression without grounding_: without communicative objectives, continued transmission converges to maximally compressible (degenerate) representations, driving P4 (non-monotonic compositionality).


These mappings allow us to derive specific predictions from the general iterated learning framework, moving beyond the generic “inductive bias amplification” characterization. Each mapping connects a well-documented LLM training property to a specific iterated learning dynamic, generating a testable prediction about which linguistic phenomena should change, in which direction, and at what relative rate.

## Appendix T Full Zipf Exponent Data

| Gen. | LLaMA-2 | Mistral |
| --- | --- | --- |
| | α\\alpha | \|V\|\|V\| | α\\alpha | \|V\|\|V\| |
| --- | --- | --- | --- | --- |
| Human∗ | 1.08 | 31,204 | — | — |
| Seed | 1.07 | 28,412 | 1.07 | 28,412 |
| 1 | 1.04 | 26,831 | 1.05 | 27,104 |
| 3 | 0.98 | 23,247 | 1.01 | 24,619 |
| 5 | 0.93 | 19,863 | 0.96 | 21,782 |
| 7 | 0.88 | 16,541 | 0.91 | 18,905 |
| 10 | 0.82 | 14,209 | 0.86 | 15,347 |
| 10QF | 0.97 | 22,847 | 0.99 | 24,113 |

Table 12: Zipf exponent (α\\alpha) and active vocabulary (\|V\|\|V\|). Means over 5 runs. The power-law fit is preferred over lognormal (Δ\\DeltaAIC >4>4) and exponential (Δ\\DeltaAIC >12>12) alternatives at all generations ( [Clauset et al., 2009](https://arxiv.org/html/2605.23054v1#bib.bib11 "")). QF: quality filter.

## Appendix U Human Regularization Overlay

111.51.5222.52.5333.53.5444.54.5555.55.56660608080100100log10\\log\_{10}(Token Frequency)Regularity Preference (%)LLM Gen. 10LLM log-linear fitHuman (M&L 2016)Human log-linear fitFigure 4: Frequency-dependent regularization gradient: LLM (blue) vs. human data from [Morgan and Levy (2016)](https://arxiv.org/html/2605.23054v1#bib.bib39 "") (red). Both follow log-linear relationships with similar slopes (−8.0-8.0 vs. −7.2-7.2), consistent with a shared computational mechanism (frequency-independent bias + transmission bottleneck). R2=0.94R^{2}=0.94 for the LLM fit.

## Appendix V Discussion: Construction Grammar and Human Parallels

The LLM–human match (R2=0.94R^{2}=0.94 against the [Morgan and Levy, 2016](https://arxiv.org/html/2605.23054v1#bib.bib39 "") curve) suggests a shared mechanism: frequency-independent simplicity bias interacting with a transmission bottleneck. Whether LLMs share functional biases with humans remains open ( [Mahowald et al., 2023](https://arxiv.org/html/2605.23054v1#bib.bib48 "")). The generation-10 “prior” (dominant SVO, regular morphology, reduced construction diversity, sub-1.0 Zipf exponents) resembles adult learner biases ( [Hudson Kam and Newport, 2005](https://arxiv.org/html/2605.23054v1#bib.bib37 ""); [Hudson Kam and Newport, 2009](https://arxiv.org/html/2605.23054v1#bib.bib38 "")); whether this more closely resembles children’s ( [Culbertson and Adger, 2014](https://arxiv.org/html/2605.23054v1#bib.bib40 "")) or adults’ learning remains open, though [Warstadt and Bowman (2022)](https://arxiv.org/html/2605.23054v1#bib.bib17 "") showed LLMs acquire syntax differently from children.

The P3 entrenchment correlation (r=0.73r=0.73) independently tests CxG predictions about productivity and resistance to loss ( [Goldberg, 2005](https://arxiv.org/html/2605.23054v1#bib.bib46 ""); [Bybee, 2010](https://arxiv.org/html/2605.23054v1#bib.bib47 "")). [Misra and Mahowald (2024)](https://arxiv.org/html/2605.23054v1#bib.bib55 "") showed LLMs learn rare constructions via transfer; our results show the converse: degradation through iterated learning makes rare constructions vulnerable. The eRank analysis confirms genuine structural erosion (eRank: 8.3→4.18.3\\to 4.1).

## Appendix W Extended Related Work

#### Compositionality and inductive biases.

Benchmarks: SCAN ( [Lake and Baroni, 2018](https://arxiv.org/html/2605.23054v1#bib.bib75 "")), COGS ( [Kim and Linzen, 2020](https://arxiv.org/html/2605.23054v1#bib.bib19 "")); meta-learning ( [Lake and Baroni, 2023](https://arxiv.org/html/2605.23054v1#bib.bib20 "")); evaluation frameworks ( [Hupkes et al., 2020](https://arxiv.org/html/2605.23054v1#bib.bib21 ""); [Keysers et al., 2020](https://arxiv.org/html/2605.23054v1#bib.bib22 "")). Emergent communication: [Lazaridou et al. (2017)](https://arxiv.org/html/2605.23054v1#bib.bib23 ""); [Lazaridou and Baroni (2020)](https://arxiv.org/html/2605.23054v1#bib.bib24 "") on language emergence; [Ren et al. (2020)](https://arxiv.org/html/2605.23054v1#bib.bib25 "") on compositionality from iterated learning; [Chaabouni et al. (2020)](https://arxiv.org/html/2605.23054v1#bib.bib13 "") on compositionality–generalization; [Mu and Goodman (2021)](https://arxiv.org/html/2605.23054v1#bib.bib26 "") on emergence conditions. Inductive biases: architecture effects ( [McCoy et al., 2020](https://arxiv.org/html/2605.23054v1#bib.bib15 "")); LLM vs. child learning ( [Warstadt and Bowman, 2022](https://arxiv.org/html/2605.23054v1#bib.bib17 "")); autoregressive biases ( [McCoy et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib54 "")); Bayesian prior distillation ( [McCoy and Griffiths, 2025](https://arxiv.org/html/2605.23054v1#bib.bib73 "")); morphological biases ( [Kallini et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib16 "")); rare construction transfer ( [Misra and Mahowald, 2024](https://arxiv.org/html/2605.23054v1#bib.bib55 "")); developmental modeling ( [Nikolaus et al., 2021](https://arxiv.org/html/2605.23054v1#bib.bib74 "")); decoding distributions ( [Holtzman et al., 2020](https://arxiv.org/html/2605.23054v1#bib.bib27 ""); [Meister et al., 2023](https://arxiv.org/html/2605.23054v1#bib.bib60 "")); predictability effects ( [Shain et al., 2024](https://arxiv.org/html/2605.23054v1#bib.bib50 "")).