[Skip to main content](https://www.nature.com/articles/s41586-024-07566-y#content)

Thank you for visiting nature.com. You are using a browser version with limited support for CSS. To obtain
the best experience, we recommend you use a more up to date browser (or turn off compatibility mode in
Internet Explorer). In the meantime, to ensure continued support, we are displaying the site without styles
and JavaScript.

AI models collapse when trained on recursively generated data


[Download PDF](https://www.nature.com/articles/s41586-024-07566-y.pdf)

[Download PDF](https://www.nature.com/articles/s41586-024-07566-y.pdf)

An [Author Correction](https://doi.org/10.1038/s41586-025-08905-3) to this article was published on 21 March 2025

This article has been [updated](https://www.nature.com/articles/s41586-024-07566-y#change-history)

## Abstract

Stable diffusion revolutionized image creation from descriptive text. GPT-2 (ref. [1](https://www.nature.com/articles/s41586-024-07566-y#ref-CR1 "Radford, A. et al. Language models are unsupervised multitask learners. OpenAI blog 1, 9 (2019).")), GPT-3(.5) (ref. [2](https://www.nature.com/articles/s41586-024-07566-y#ref-CR2 "Brown, T. et al. Language models are few-shot learners. Adv. Neural Inf. Process. Syst. 33, 1877–1901 (2020).")) and GPT-4 (ref. [3](https://www.nature.com/articles/s41586-024-07566-y#ref-CR3 "OpenAI. GPT-4 Technical Report. https://cdn.openai.com/papers/gpt-4.pdf (2023).")) demonstrated high performance across a variety of language tasks. ChatGPT introduced such language models to the public. It is now clear that generative artificial intelligence (AI) such as large language models (LLMs) is here to stay and will substantially change the ecosystem of online text and images. Here we consider what may happen to GPT-{ _n_} once LLMs contribute much of the text found online. We find that indiscriminate use of model-generated content in training causes irreversible defects in the resulting models, in which tails of the original content distribution disappear. We refer to this effect as ‘model collapse’ and show that it can occur in LLMs as well as in variational autoencoders (VAEs) and Gaussian mixture models (GMMs). We build theoretical intuition behind the phenomenon and portray its ubiquity among all learned generative models. We demonstrate that it must be taken seriously if we are to sustain the benefits of training from large-scale data scraped from the web. Indeed, the value of data collected about genuine human interactions with systems will be increasingly valuable in the presence of LLM-generated content in data crawled from the Internet.

### Similar content being viewed by others

![](https://media.springernature.com/w215h120/springer-static/image/art%3A10.1038%2Fs41598-024-61221-0/MediaObjects/41598_2024_61221_Fig1_HTML.png)

### [The consequences of generative AI for online knowledge communities](https://www.nature.com/articles/s41598-024-61221-0?fromPaywallRec=false)

ArticleOpen access06 May 2024

![](https://media.springernature.com/w215h120/springer-static/image/art%3Aplaceholder%2Fimages/placeholder-figure-nature.png)

### [Large language models are proficient in solving and creating emotional intelligence tests](https://www.nature.com/articles/s44271-025-00258-x?fromPaywallRec=false)

ArticleOpen access21 May 2025

![](https://media.springernature.com/w215h120/springer-static/image/art%3A10.1038%2Fs44183-025-00132-7/MediaObjects/44183_2025_132_Fig1_HTML.png)

### [AI language models could both help and harm equity in marine policymaking](https://www.nature.com/articles/s44183-025-00132-7?fromPaywallRec=false)

ArticleOpen access11 June 2025

### Explore related subjects

Discover the latest articles and news in related subjects.

- [Computational science](https://www.nature.com/subjects/computational-science)
- [Computer science](https://www.nature.com/subjects/computer-science)
- [Natural Language Processing Techniques for Sentiment Analysis](https://www.nature.com/subjects/natural-language-processing-techniques-for-sentiment-analysis)

## Main

The development of LLMs is very involved and requires large quantities of training data. Yet, although current LLMs[2](https://www.nature.com/articles/s41586-024-07566-y#ref-CR2 "Brown, T. et al. Language models are few-shot learners. Adv. Neural Inf. Process. Syst. 33, 1877–1901 (2020)."), [4](https://www.nature.com/articles/s41586-024-07566-y#ref-CR4 "Devlin, J., Chang, M.-W., Lee, K. & Toutanova, K. in Proc. 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers) (eds Burstein, J., Doran, C. & Solorio, T.) 4171–4186 (Association for Computational Linguistics, 2019)."), [5](https://www.nature.com/articles/s41586-024-07566-y#ref-CR5 "Liu, Y. et al. RoBERTa: a Robustly Optimized BERT Pretraining Approach. Preprint at https://arxiv.org/abs/1907.11692 (2019)."), [6](https://www.nature.com/articles/s41586-024-07566-y#ref-CR6 "Zhang, S. et al. Opt: open pre-trained transformer language models. Preprint at https://arxiv.org/abs/2205.01068 (2022)."), including GPT-3, were trained on predominantly human-generated text, this may change. If the training data of most future models are also scraped from the web, then they will inevitably train on data produced by their predecessors. In this paper, we investigate what happens when text produced by, for example, a version of GPT forms most of the training dataset of following models. What happens to GPT generations GPT-{ _n_} as _n_ increases? We discover that indiscriminately learning from data produced by other models causes ‘model collapse’—a degenerative process whereby, over time, models forget the true underlying data distribution, even in the absence of a shift in the distribution over time. We give examples of model collapse for GMMs, VAEs and LLMs. We show that, over time, models start losing information about the true distribution, which first starts with tails disappearing, and learned behaviours converge over the generations to a point estimate with very small variance. Furthermore, we show that this process is inevitable, even for cases with almost ideal conditions for long-term learning, that is, no function estimation error. We also briefly mention two close concepts to model collapse from the existing literature: catastrophic forgetting arising in the framework of task-free continual learning[7](https://www.nature.com/articles/s41586-024-07566-y#ref-CR7 "Aljundi, R., Kelchtermans, K. & Tuytelaars, T. Task-free continual learning. in: Proc. 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) 11254–11263 (IEEE, 2019).") and data poisoning[8](https://www.nature.com/articles/s41586-024-07566-y#ref-CR8 "Carlini, N. & Terzis, A. in Proc. Tenth International Conference on Learning Representations (ICLR, 2022)."), [9](https://www.nature.com/articles/s41586-024-07566-y#ref-CR9 "Carlini, N. et al. in Proc. 2024 IEEE Symposium on Security and Privacy (SP) 179 (IEEE, 2024).") maliciously leading to unintended behaviour. Neither is able to explain the phenomenon of model collapse fully, as the setting is fundamentally different, but they provide another perspective on the observed phenomenon and are discussed in more depth in the [Supplementary Materials](https://www.nature.com/articles/s41586-024-07566-y#MOESM1). Finally, we discuss the broader implications of model collapse. We note that access to the original data distribution is crucial: in learning tasks in which the tails of the underlying distribution matter, one needs access to real human-produced data. In other words, the use of LLMs at scale to publish content on the Internet will pollute the collection of data to train their successors: data about human interactions with LLMs will be increasingly valuable.

## What is model collapse?

### Definition 2.1 (model collapse)

Model collapse is a degenerative process affecting generations of learned generative models, in which the data they generate end up polluting the training set of the next generation. Being trained on polluted data, they then mis-perceive reality. The process is depicted in Fig. [1a](https://www.nature.com/articles/s41586-024-07566-y#Fig1). We separate two special cases: early model collapse and late model collapse. In early model collapse, the model begins losing information about the tails of the distribution; in late model collapse, the model converges to a distribution that carries little resemblance to the original one, often with substantially reduced variance.

This process occurs owing to three specific sources of error compounding over generations and causing deviation from the original model:

- **Statistical approximation error.** This is the primary type of error, which arises owing to the number of samples being finite, and disappears as the number of samples tends to infinity. This occurs because of a non-zero probability that information can get lost at every step of resampling.

- **Functional expressivity error.** This is a secondary type of error, arising owing to limited function approximator expressiveness. In particular, neural networks are only universal approximators as their size goes to infinity. As a result, a neural network can introduce non-zero likelihood outside the support of the original distribution or zero likelihood inside the support of the original distribution. A simple example of the expressivity error is if we tried fitting a mixture of two Gaussians with a single Gaussian. Even if we have perfect information about the data distribution (that is, infinite number of samples), model errors will be inevitable. However, in the absence of the other two types of error, this can only occur at the first generation.

- **Functional approximation error.** This is a secondary type of error, arising primarily from the limitations of learning procedures, for example, structural bias of stochastic gradient descent[10](https://www.nature.com/articles/s41586-024-07566-y#ref-CR10 "Mousavi-Hosseini, A., Park, S., Girotti, M., Mitliagkas, I. & Erdogdu, M. A. in Proc. Eleventh International Conference on Learning Representations (ICLR, 2023)."), [11](https://www.nature.com/articles/s41586-024-07566-y#ref-CR11 "Soudry, D., Hoffer, E., Nacson, M. S., Gunasekar, S. & Srebro, N. The implicit bias of gradient descent on separable data. J. Mach. Learn. Res. 19, 1–57 (2018).") or choice of objective[12](https://www.nature.com/articles/s41586-024-07566-y#ref-CR12 "Gu, Y., Dong, L., Wei, F. & Huang, M. in Proc. Twelfth International Conference on Learning Representations (ICLR, 2024)."). This error can be viewed as one arising in the limit of infinite data and perfect expressivity at each generation.


Each of the above can cause model collapse to get worse or better. More approximation power can even be a double-edged sword—better expressiveness may counteract statistical noise, resulting in a good approximation of the true distribution, but it can equally compound the noise. More often than not, we get a cascading effect, in which individual inaccuracies combine to cause the overall error to grow. For example, overfitting the density model causes the model to extrapolate incorrectly and assigns high-density regions to low-density regions not covered in the training set support; these will then be sampled with arbitrary frequency. It is worth noting that other types of error exist. For example, computers have limited precision in practice. We now turn to mathematical intuition to explain how the above give rise to the errors observed, how different sources can compound and how we can quantify the average model divergence.

## Theoretical intuition

Here we provide a theoretical intuition for the phenomenon of model collapse. We argue that the process of model collapse is universal among generative models that recursively train on data generated by previous generations. We quantify the sources of errors discussed in the previous section by examining two mathematical models, which prove to be simple enough to provide analytical expressions for quantities of interest, but also portray the phenomenon of model collapse: a discrete distribution in the absence of functional expressivity and approximation errors, and a multidimensional Gaussian approximation, portraying joint functional expressivity and statistical errors. We further illustrate the impact of all three jointly for a more complex setting of density estimation in Hilbert spaces in the [Supplementary Materials](https://www.nature.com/articles/s41586-024-07566-y#MOESM1).

The overall stochastic process we consider, which we call learning with generational data, is the following. The dataset at generation _i_ is Di, comprising independent and identically distributed random variables Xji with distribution _p_ _i_, _j_ ∈ {1,…, _M_ _i_} denotes the size of the dataset. Going from generation _i_ to generation _i_ + 1, we aim to estimate the distribution of samples in Di, with an approximation pθi+1. This step is what we refer to as functional approximation, pθi+1=Fθ(pi). The dataset Di+1 is then generated by sampling from pi+1=αipθi+1+βipi+γip0, with non-negative parameters _α_ _i_, _β_ _i_, _γ_ _i_ summing to 1, that is, they represent proportions of data used from different generations. This corresponds to a mixing of data coming from the original distribution ( _γ_ _i_), data used by the previous generation ( _β_ _i_) and data generated by the new model ( _α_ _i_). We refer to this as the sampling step. For the mathematical models to come, we consider _β_ _i_ = _γ_ _i_ = 0, that is, data only from a single step are used, whereas numerical experiments are performed on more realistic choices of parameters.

### Discrete distributions with exact approximation

In this subsection, we consider a discrete probability distribution in absence of functional approximation and expressivity errors, that is, F(p)=p. In this case, model collapse arises only because of statistical errors from the sampling step. At first, the tails (low-probability events) begin to disappear as a result of the low probability of sampling them and, over time, support of the distribution shrinks. Denoting the sample size as _M_, if we consider state _i_ with probability q≤1M, the expected number of samples with value _i_ coming from those events will be less than 1. In practice, this would mean that we lose information about them. Considering more generally some state _i_ with probability _q_, using standard conditional probability, we can show that the probability of losing information (that is, sampling no data at some generation) is equal to 1 − _q_, implying that the distribution must converge to a delta function positioned at some state, with the probability of ending up at a certain state equal to the probability of sampling said state from the original distribution.

This can be shown directly by considering the process Xi→F→pi+1→Xi+1 as a Markov chain, as **X** _i_ +1 only depends on **X** _i_. Furthermore, if all the Xji have the same value, then at the next generation, the approximated distribution will be exactly a delta function and therefore all of Xji+1 will also have the same value. This implies that the Markov chain contains at least one absorbing state and therefore, with probability 1, it will converge to one of the absorbing states. This is a well-known fact, of which a proof is provided in the [Supplementary Materials](https://www.nature.com/articles/s41586-024-07566-y#MOESM1). For this chain, the only absorbing states are those corresponding to delta functions. As a result, as we follow the progress of model collapse, we are guaranteed to end up in a constant state, having lost all the information of the original distribution when the chain is absorbed. This argument also works in general owing to floating-point representations being discrete, making the Markov chain over the parameters of the model discrete. Thus, as long as the model parameterization allows for delta functions, we will get to it, because—owing to sampling errors—the only possible absorbing states are delta functions. On the basis of the discussion above, we see how both early model collapse, in which only the low-probability events get cut off, and late stage model collapse, in which the process begins to collapse into a single mode, must arise in the case of discrete distributions with perfect functional approximation.

### Multidimensional Gaussian

Following the discussion about discrete distributions, we now present a more generic result, which can be shown in the Gaussian approximation setting, in which each generation is approximated using the unbiased estimates of the mean and the variance. A similar result holds more generally, which we detail in the [Supplementary Materials](https://www.nature.com/articles/s41586-024-07566-y#MOESM1).

### Theorem 3.1 (Gaussian model collapse)

Assume the original data are sampled from distribution D0 (not necessarily Gaussian), with non-zero sample variance. Assume _X_ _n_ are fit recursively using the unbiased sample mean and variance estimators from the previous generation, Xjn\|μn,Σn∼N(μn,Σn), with a fixed sample size. Then,

E\[W22(N(μn,Σn),D0)\]→∞;Σn→a.s.0asn→∞,

in which W2 denotes the Wasserstein-2 distance between the true distribution and its approximation at generation _n_.

In words, this implies that not only does the _n_ th generation approximation diverge arbitrarily far from the original one but it also collapses to be zero variance as the number of generations increases, with probability 1. The results are very analogous to that seen in the discrete case, with this theorem illustrating the effect of late stage model collapse, in which the process begins to collapse to be zero variance. The early stage model collapse can also be seen and the interested reader is referred to the [Supplementary Materials](https://www.nature.com/articles/s41586-024-07566-y#MOESM1) for a more in-depth discussion.

## Model collapse in language models

In this section, we evaluate the effect of model collapse on language models. We cover more interpretable machine learning models—VAEs and GMMs—in the [Supplementary Materials](https://www.nature.com/articles/s41586-024-07566-y#MOESM1). Code is publically available in ref. [13](https://www.nature.com/articles/s41586-024-07566-y#ref-CR13 "Shumailov, I. & Shumaylov, Z. Public code for Model Collapse (0.1). Zenodo https://doi.org/10.5281/zenodo.10866595 (2024).").

Model collapse is universal across various families of machine learning models. Yet, if small models such as GMMs and VAEs are normally trained from scratch, LLMs are different. They are so expensive to retrain from scratch that they are typically initialized with pre-trained models such as BERT[4](https://www.nature.com/articles/s41586-024-07566-y#ref-CR4 "Devlin, J., Chang, M.-W., Lee, K. & Toutanova, K. in Proc. 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers) (eds Burstein, J., Doran, C. & Solorio, T.) 4171–4186 (Association for Computational Linguistics, 2019)."), RoBERTa[5](https://www.nature.com/articles/s41586-024-07566-y#ref-CR5 "Liu, Y. et al. RoBERTa: a Robustly Optimized BERT Pretraining Approach. Preprint at https://arxiv.org/abs/1907.11692 (2019).") or GPT-2 (ref. [2](https://www.nature.com/articles/s41586-024-07566-y#ref-CR2 "Brown, T. et al. Language models are few-shot learners. Adv. Neural Inf. Process. Syst. 33, 1877–1901 (2020).")), which are trained on large text corpora. They are then fine-tuned to various downstream tasks[14](https://www.nature.com/articles/s41586-024-07566-y#ref-CR14 "Bommasani, R. et al. On the opportunities and risks of foundation models. Preprint at https://arxiv.org/abs/2108.07258 (2022).").

Here we explore what happens with language models when they are sequentially fine-tuned with data generated by other models. We can easily replicate all experiments covered in this paper with larger language models in non-fine-tuning settings to demonstrate model collapse. Given that training a single moderately large model produces twice the American lifetime’s worth of CO2 (ref. [15](https://www.nature.com/articles/s41586-024-07566-y#ref-CR15 "Strubell, E., Ganesh, A. & McCallum, A. in Proc. 57th Annual Meeting of the Association for Computational Linguistics (eds Korhonen, A., Traum, D. & Màrquez, L.) 3645–3650 (Association for Computational Linguistics, 2019).")), we opted to not run such an experiment and instead focus on a more realistic setting for a proof of concept. Note that even the language experiments described in this paper took weeks to run. We evaluate the most common setting of training a language model—a fine-tuning setting for which each of the training cycles starts from a pre-trained model with recent data. The data here come from another fine-tuned pre-trained model. Because training is restricted to produce models that are close to the original pre-trained model, and data points generated by the models will generally produce very small gradients, the expectation here may be that the model should only change moderately after fine-tuning. We fine-tune the OPT-125m causal language model made available by Meta through Hugging Face[6](https://www.nature.com/articles/s41586-024-07566-y#ref-CR6 "Zhang, S. et al. Opt: open pre-trained transformer language models. Preprint at https://arxiv.org/abs/2205.01068 (2022).").

We fine-tune it on the wikitext2 dataset[16](https://www.nature.com/articles/s41586-024-07566-y#ref-CR16 "Merity, S., Xiong, C., Bradbury, J. & Socher, R. in Proc. 5th International Conference on Learning Representations (ICLR, 2017)."). For data generation from the trained models, we use a five-way beam search. We block training sequences to be 64 tokens long; then, for each token sequence in the training set, we ask the model to predict the next 64 tokens. We go through all of the original training dataset and produce an artificial dataset of the same size. Because we go through all of the original dataset and predict all of the blocks, if the model had 0 error, it would produce the original wikitext2 dataset. Training for each generation starts with generation from the original training data. Each experiment is run five times and the results are shown as five separate runs with different randomness seeds. The original model fine-tuned with real wikitext2 data obtains 34 mean perplexity, from the zero-shot baseline of 115, that is, it successfully learns the task. Finally, to be as realistic as possible, we use the best-performing model on the original task, evaluated using the original wikitext2 validation set, as the base model for the subsequent generations, meaning that—in practice—observed model collapse can be even more pronounced. Here we consider two different settings:

- Five epochs, no original training data. Here the model is trained for five epochs starting on the original dataset but with no original data retained for subsequent runs. The overall original task performance is presented in Fig. [1b](https://www.nature.com/articles/s41586-024-07566-y#Fig1). We find that training with generated data allows us to adapt to the underlying task, losing some performance, from 20 to 28 perplexity points.

- Ten epochs, 10% of original training data preserved. Here the model is trained for ten epochs on the original dataset and with every new generation of training, a random 10% of the original data points is sampled. The overall original task performance is presented in Fig. [1c](https://www.nature.com/articles/s41586-024-07566-y#Fig1). We find that preservation of the original data allows for better model fine-tuning and leads to only minor degradation of performance.


Both training regimes lead to degraded performance in our models, yet we do find that learning with generated data is possible and models can successfully learn (some of) the underlying task. In particular, from Fig. [1](https://www.nature.com/articles/s41586-024-07566-y#Fig1) and their 3D versions in the [Supplementary Materials](https://www.nature.com/articles/s41586-024-07566-y#MOESM1), we see that model collapse occurs, as the density of samples with low perplexity begins to accumulate over the generations. This in turn makes it likely that, over the generations, the sampled data will similarly collapse to a delta function.

**Fig. 1: The high-level description of the feedback mechanism in the learning process.**

![Fig. 1: The high-level description of the feedback mechanism in the learning process.](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41586-024-07566-y/MediaObjects/41586_2024_7566_Fig1_HTML.png)

[Full size image](https://www.nature.com/articles/s41586-024-07566-y/figures/1)

**a**, Model collapse refers to a degenerative learning process in which models start forgetting improbable events over time, as the model becomes poisoned with its own projection of reality. Here data are assumed to be human-curated and start off clean; then model 0 is trained and data are sampled from it; at step _n_, data are added to the overall data from step _n_ − 1 and this combination is used to train model _n_. Data obtained with Monte Carlo sampling should ideally be statistically close to the original, provided that fitting and sampling procedures are perfect. This process depicts what happens in real life with the Internet: model-generated data become pervasive. **b**, **c**, Performance of OPT-125m models of different generations evaluated using the original wikitext2 test dataset. Shown on the left are the histograms of perplexities of each individual data training sequence produced by different generations as evaluated by the very first model trained with the real data. Over the generations, models tend to produce samples that the original model trained with real data is more likely to produce. At the same time, a much longer tail appears for later generations. Later generations start producing samples that would never be produced by the original model, that is, they start misperceiving reality based on errors introduced by their ancestors. The same plots are shown in 3D in the [Supplementary Materials](https://www.nature.com/articles/s41586-024-07566-y#MOESM1). On the right, average perplexity and its standard deviation are shown for each independent run. The _x_ axis refers to the generation of the model. ‘Real’ refers to the ‘model 0’ trained on the original wikitext2 dataset; model 1 was trained on the data produced by model 0, model 2 was trained on data produced by model 1 and so on, with all generated datasets equal in size. We find that models trained on generated data are able to learn some of the original task, but with errors, as seen from the increase in perplexity.

It is important to note here that the observed behaviour is in line with the general intuition established in the section ‘Theoretical intuition’. To be precise, in all experiments, generational learning is only performed on a finite (usually small) number of generations, whereas claims of the section ‘Theoretical intuition’ are mostly presented in the limit of generations going to infinity. However, as seen from experiments on VAEs and GMMs in the [Supplementary Materials](https://www.nature.com/articles/s41586-024-07566-y#MOESM1), convergence to delta functions and specific rates of such convergence are highly related to the specifics of the problem considered, and complete collapse may or may not occur, even after a small number of steps. This is further illustrated theoretically in the [Supplementary Materials](https://www.nature.com/articles/s41586-024-07566-y#MOESM1), in which potentially notable divergence from the original model can occur even after a few generations.

Figure [1b,c](https://www.nature.com/articles/s41586-024-07566-y#Fig1) on the left shows histograms of individual data-point perplexities generated by the models of different generations as is evaluated by the first model developed with real wikitext2 training data. Here, over the generations, models tend to produce more sequences that the original model would produce with the higher likelihood. The observed effect is similar to that described for VAEs and GMMs in the [Supplementary Materials](https://www.nature.com/articles/s41586-024-07566-y#MOESM1), in which—over the generations—models started to produce samples that would be produced with higher probabilities by the original model. At the same time, we discover that generated data have much longer tails, suggesting that some of the data would never be produced by the original model—these are the errors that accumulate because of the learning with generational data.

### Example 1

Example of text outputs of an OPT-125m model affected by model collapse—models degrade over generations, for which each new generation is trained on data produced by the previous generation.

- **Input:** some started before 1360 — was typically accomplished by a master mason and a small team of itinerant masons, supplemented by local parish labourers, according to Poyntz Wright. But other authors reject this model, suggesting instead that leading architects designed the parish church towers based on early examples of Perpendicular.

- **Outputs:**

- **Gen 0:** Revival architecture such as St. John’s Cathedral in London. The earliest surviving example of Perpendicular Revival architecture is found in the 18th @-@ century Church of Our Lady of Guernsey, which dates from the late 19th century. There are two types of perpendicular churches : those.

- **Gen 1:** architecture such as St. Peter’s Basilica in Rome or St. Peter’s Basilica in Buenos Aires. There is no evidence that any of these buildings were built during the reign of Pope Innocent III, but it is possible that they may have been built during the reign of his successor, Pope Innocent.

- **Gen 5:** ism, which had been translated into more than 100 languages including English, French, German, Italian, Spanish, Portuguese, Dutch, Swedish, Norwegian, Polish, Hungarian, Slovak, Lithuanian, Estonian, Finnish, Romanian, Bulgarian, Turkish, Croatian, Serbian, Ukrainian, Russian, Kazakh, Kyrgyz.

- **Gen 9:** architecture. In addition to being home to some of the world’s largest populations of black @-@ tailed jackrabbits, white @-@ tailed jackrabbits, blue @-@ tailed jackrabbits, red @-@ tailed jackrabbits, yellow @-.


### Ablation: Repetitions

We find that data generated by language models in our experiments end up containing a large number of repeating phrases, as in Example 1. The repeating problem has been observed in nearly all text-generation models[17](https://www.nature.com/articles/s41586-024-07566-y#ref-CR17 "Keskar, N. S., McCann, B., Varshney, L. R., Xiong, C. & Socher, R. CTRL: a conditional transformer language model for controllable generation. Preprint at https://arxiv.org/abs/1909.05858 (2019)."), [18](https://www.nature.com/articles/s41586-024-07566-y#ref-CR18 "Shumailov, I. et al. in Proc. 2021 IEEE European Symposium on Security and Privacy (EuroS&P) 212–231 (IEEE, 2021).") and, to rule this out as the cause of model collapse, we further provide numerical experiments when models are explicitly encouraged to produce non-repeating sequences with a repeating penalty of 2.0. We find that this causes the models to produce lower score continuations to avoid using repeats, which—as a result—causes the consequent models to perform even worse. Model perplexities shift across the generations towards more probable token sequences, as measured using the model trained on the original real data distribution. Further illustrations are provided in the [Supplementary Materials](https://www.nature.com/articles/s41586-024-07566-y#MOESM1). In particular, enforcing this for the LLM experiments causes the perplexity to double compared with the original. Models remain as susceptible to model collapse, if not more.

The described process demonstrates that fine-tuning of language models does not curb the effects of model collapse and models that are being fine-tuned are also vulnerable. We find that, over the generations, models tend to produce more probable sequences from the original data and start introducing their own improbable sequences, that is, errors.

## Discussion

We now discuss the implications of model collapse on the underlying learning dynamics of LLMs. Long-term poisoning attacks on language models are not new. For example, we saw the creation of click, content and troll farms, a form of human ‘language models’, whose job is to misguide social networks and search algorithms. The negative effect that these poisoning attacks had on search results led to changes in search algorithms. For example, Google downgraded farmed articles[19](https://www.nature.com/articles/s41586-024-07566-y#ref-CR19 "Google. Finding more high-quality sites in search. Google https://googleblog.blogspot.com/2011/02/finding-more-high-quality-sites-in.html (2011)."), putting more emphasis on content produced by trustworthy sources, such as education domains, whereas DuckDuckGo removed them altogether[20](https://www.nature.com/articles/s41586-024-07566-y#ref-CR20 "Mims, C. The search engine backlash against ‘content mills’. MIT Technology Review https://www.technologyreview.com/2010/07/26/26327/the-search-engine-backlash-against-content-mills/ (2010)."). What is different with the arrival of LLMs is the scale at which such poisoning can happen once it is automated. Preserving the ability of LLMs to model low-probability events is essential to the fairness of their predictions: such events are often relevant to marginalized groups. Low-probability events are also vital to understand complex systems[21](https://www.nature.com/articles/s41586-024-07566-y#ref-CR21 "Taleb, N. N. Black swans and the domains of statistics. Am. Stat. 61, 198–200 (2007).").

Our evaluation suggests a ‘first mover advantage’ when it comes to training models such as LLMs. In our work, we demonstrate that training on samples from another generative model can induce a distribution shift, which—over time—causes model collapse. This in turn causes the model to mis-perceive the underlying learning task. To sustain learning over a long period of time, we need to make sure that access to the original data source is preserved and that further data not generated by LLMs remain available over time. The need to distinguish data generated by LLMs from other data raises questions about the provenance of content that is crawled from the Internet: it is unclear how content generated by LLMs can be tracked at scale. One option is community-wide coordination to ensure that different parties involved in LLM creation and deployment share the information needed to resolve questions of provenance. Otherwise, it may become increasingly difficult to train newer versions of LLMs without access to data that were crawled from the Internet before the mass adoption of the technology or direct access to data generated by humans at scale.

## Data availability

Data generation code for GMM experiments is available in ref. [13](https://www.nature.com/articles/s41586-024-07566-y#ref-CR13 "Shumailov, I. & Shumaylov, Z. Public code for Model Collapse (0.1). Zenodo https://doi.org/10.5281/zenodo.10866595 (2024)."). Data used for VAE experiments are available in ref. [22](https://www.nature.com/articles/s41586-024-07566-y#ref-CR22 "LeCun, Y., Cortes, C. & Burges, C. J. C. The MNIST database of handwritten digits. http://yann.lecun.com/exdb/mnist/ (1998)."). Data used for LLM experiments are available in ref. [16](https://www.nature.com/articles/s41586-024-07566-y#ref-CR16 "Merity, S., Xiong, C., Bradbury, J. & Socher, R. in Proc. 5th International Conference on Learning Representations (ICLR, 2017).").

## Code availability

Code for all experiments is publically available in ref. [13](https://www.nature.com/articles/s41586-024-07566-y#ref-CR13 "Shumailov, I. & Shumaylov, Z. Public code for Model Collapse (0.1). Zenodo https://doi.org/10.5281/zenodo.10866595 (2024).").

## Change history

- ### 21 March 2025





A Correction to this paper has been published: [https://doi.org/10.1038/s41586-025-08905-3](https://doi.org/10.1038/s41586-025-08905-3)


## References

01. Radford, A. et al. Language models are unsupervised multitask learners. _OpenAI blog_ **1**, 9 (2019).

 [MATH](http://www.emis.de/MATH-item?0446.16009) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Language%20models%20are%20unsupervised%20multitask%20learners&journal=OpenAI%20blog&volume=1&publication_year=2019&author=Radford%2CA)

02. Brown, T. et al. Language models are few-shot learners. _Adv. Neural Inf. Process. Syst._ **33**, 1877–1901 (2020).

 [MATH](http://www.emis.de/MATH-item?0816.16014) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Language%20models%20are%20few-shot%20learners&journal=Adv.%20Neural%20Inf.%20Process.%20Syst.&volume=33&pages=1877-1901&publication_year=2020&author=Brown%2CT)

03. OpenAI. GPT-4 Technical Report. [https://cdn.openai.com/papers/gpt-4.pdf](https://cdn.openai.com/papers/gpt-4.pdf) (2023).

04. Devlin, J., Chang, M.-W., Lee, K. & Toutanova, K. in _Proc. 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)_ (eds Burstein, J., Doran, C. & Solorio, T.) 4171–4186 (Association for Computational Linguistics, 2019).

05. Liu, Y. et al. RoBERTa: a Robustly Optimized BERT Pretraining Approach. Preprint at [https://arxiv.org/abs/1907.11692](https://arxiv.org/abs/1907.11692) (2019).

06. Zhang, S. et al. Opt: open pre-trained transformer language models. Preprint at [https://arxiv.org/abs/2205.01068](https://arxiv.org/abs/2205.01068) (2022).

07. Aljundi, R., Kelchtermans, K. & Tuytelaars, T. Task-free continual learning. in: _Proc. 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)_ 11254–11263 (IEEE, 2019).

08. Carlini, N. & Terzis, A. in _Proc. Tenth International Conference on Learning Representations_ (ICLR, 2022).

09. Carlini, N. et al. in _Proc. 2024 IEEE Symposium on Security and Privacy (SP)_ 179 (IEEE, 2024).

10. Mousavi-Hosseini, A., Park, S., Girotti, M., Mitliagkas, I. & Erdogdu, M. A. in _Proc. Eleventh International Conference on Learning Representations_ (ICLR, 2023).

11. Soudry, D., Hoffer, E., Nacson, M. S., Gunasekar, S. & Srebro, N. The implicit bias of gradient descent on separable data. _J. Mach. Learn. Res._ **19**, 1–57 (2018).

 [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=3899772) [MATH](http://www.emis.de/MATH-item?1477.62192) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20implicit%20bias%20of%20gradient%20descent%20on%20separable%20data&journal=J.%20Mach.%20Learn.%20Res.&volume=19&pages=1-57&publication_year=2018&author=Soudry%2CD&author=Hoffer%2CE&author=Nacson%2CMS&author=Gunasekar%2CS&author=Srebro%2CN)

12. Gu, Y., Dong, L., Wei, F. & Huang, M. in _Proc. Twelfth International Conference on Learning Representations_ (ICLR, 2024).

13. Shumailov, I. & Shumaylov, Z. Public code for Model Collapse (0.1). _Zenodo_ [https://doi.org/10.5281/zenodo.10866595](https://doi.org/10.5281/zenodo.10866595) (2024).

14. Bommasani, R. et al. On the opportunities and risks of foundation models. Preprint at [https://arxiv.org/abs/2108.07258](https://arxiv.org/abs/2108.07258) (2022).

15. Strubell, E., Ganesh, A. & McCallum, A. in _Proc. 57th Annual Meeting of the Association for Computational Linguistics_ (eds Korhonen, A., Traum, D. & Màrquez, L.) 3645–3650 (Association for Computational Linguistics, 2019).

16. Merity, S., Xiong, C., Bradbury, J. & Socher, R. in _Proc. 5th International Conference on Learning Representations_ (ICLR, 2017).

17. Keskar, N. S., McCann, B., Varshney, L. R., Xiong, C. & Socher, R. CTRL: a conditional transformer language model for controllable generation. Preprint at [https://arxiv.org/abs/1909.05858](https://arxiv.org/abs/1909.05858) (2019).

18. Shumailov, I. et al. in _Proc. 2021 IEEE European Symposium on Security and Privacy (EuroS&P)_ 212–231 (IEEE, 2021).

19. Google. Finding more high-quality sites in search. _Google_ [https://googleblog.blogspot.com/2011/02/finding-more-high-quality-sites-in.html](https://googleblog.blogspot.com/2011/02/finding-more-high-quality-sites-in.html) (2011).

20. Mims, C. The search engine backlash against ‘content mills’. _MIT Technology Review_ [https://www.technologyreview.com/2010/07/26/26327/the-search-engine-backlash-against-content-mills/](https://www.technologyreview.com/2010/07/26/26327/the-search-engine-backlash-against-content-mills/) (2010).

21. Taleb, N. N. Black swans and the domains of statistics. _Am. Stat._ **61**, 198–200 (2007).

 [Article](https://doi.org/10.1198%2F000313007X219996) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=2393721) [MATH](http://www.emis.de/MATH-item?0990.65020) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Black%20swans%20and%20the%20domains%20of%20statistics&journal=Am.%20Stat.&doi=10.1198%2F000313007X219996&volume=61&pages=198-200&publication_year=2007&author=Taleb%2CNN)

22. LeCun, Y., Cortes, C. & Burges, C. J. C. The MNIST database of handwritten digits. [http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/) (1998).


[Download references](https://citation-needed.springer.com/v2/references/10.1038/s41586-024-07566-y?format=refman&flavour=references)

## Acknowledgements

This paper is dedicated to the memory of Professor Ross J. Anderson, our colleague and friend, who contributed much to this and other works we have produced over the years. We thank A. Thudi, D. Glukhov, P. Zaika, and D. Barak for useful discussions and feedback.

## Author information

Author notes

1. These authors contributed equally: Ilia Shumailov, Zakhar Shumaylov

2. Deceased: Ross Anderson


### Authors and Affiliations

1. OATML, Department of Computer Science, University of Oxford, Oxford, UK

Ilia Shumailov & Yarin Gal

2. Department of Applied Mathematics and Theoretical Physics, University of Cambridge, Cambridge, UK

Zakhar Shumaylov

3. Department of Electrical and Electronic Engineering, Imperial College London, London, UK

Yiren Zhao

4. University of Toronto, Toronto, Ontario, Canada

Nicolas Papernot

5. Vector Institute, Toronto, Ontario, Canada

Nicolas Papernot

6. Department of Computer Science and Technology, University of Cambridge, Cambridge, UK

Ross Anderson

7. School of Informatics, University of Edinburgh, Edinburgh, UK

Ross Anderson


Authors

1. Ilia Shumailov


[View author publications](https://www.nature.com/search?author=Ilia%20Shumailov)





Search author on:[PubMed](https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Ilia%20Shumailov) [Google Scholar](https://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Ilia%20Shumailov%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

2. Zakhar Shumaylov


[View author publications](https://www.nature.com/search?author=Zakhar%20Shumaylov)





Search author on:[PubMed](https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Zakhar%20Shumaylov) [Google Scholar](https://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Zakhar%20Shumaylov%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

3. Yiren Zhao


[View author publications](https://www.nature.com/search?author=Yiren%20Zhao)





Search author on:[PubMed](https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Yiren%20Zhao) [Google Scholar](https://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Yiren%20Zhao%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

4. Nicolas Papernot


[View author publications](https://www.nature.com/search?author=Nicolas%20Papernot)





Search author on:[PubMed](https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Nicolas%20Papernot) [Google Scholar](https://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Nicolas%20Papernot%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

5. Ross Anderson


[View author publications](https://www.nature.com/search?author=Ross%20Anderson)





Search author on:[PubMed](https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Ross%20Anderson) [Google Scholar](https://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Ross%20Anderson%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)

6. Yarin Gal


[View author publications](https://www.nature.com/search?author=Yarin%20Gal)





Search author on:[PubMed](https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Yarin%20Gal) [Google Scholar](https://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Yarin%20Gal%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)


### Contributions

I.S. and Z.S. proposed and developed the idea, led the research and mathematical modelling and developed the GMM and VAE experiments. I.S. and Y.Z. developed the language-model experiments. N.P., Y.G. and R.A. supervised and guided the project. All authors contributed to writing of the manuscript. Y.G. is supported by a Turing AI Fellowship financed by the UK government’s Office for Artificial Intelligence, through UK Research and Innovation (grant reference EP/V030302/1) and delivered by the Alan Turing Institute.

### Corresponding authors

Correspondence to
[Ilia Shumailov](mailto:ilia.shumailov@chch.ox.ac.uk), [Zakhar Shumaylov](mailto:zs334@cam.ac.uk) or [Yarin Gal](mailto:yarin@cs.ox.ac.uk).

## Ethics declarations

### Competing interests

The authors declare no competing interests.

## Peer review

### Peer review information

_Nature_ thanks the anonymous reviewers for their contribution to the peer review of this work.

## Additional information

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Supplementary information

### [Supplementary Information (download PDF )](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-024-07566-y/MediaObjects/41586_2024_7566_MOESM1_ESM.pdf)

### [Supplementary Data (download ZIP )](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-024-07566-y/MediaObjects/41586_2024_7566_MOESM2_ESM.zip)

## Rights and permissions

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/).

[Reprints and permissions](https://s100.copyright.com/AppDispatchServlet?title=AI%20models%20collapse%20when%20trained%20on%20recursively%20generated%20data&author=Ilia%20Shumailov%20et%20al&contentID=10.1038%2Fs41586-024-07566-y&copyright=The%20Author%28s%29&publication=0028-0836&publicationDate=2024-07-24&publisherName=SpringerNature&orderBeanReset=true&oa=CC%20BY)

## About this article

[![Check for updates. Verify currency and authenticity via CrossMark](<Base64-Image-Removed>)](https://crossmark.crossref.org/dialog/?doi=10.1038/s41586-024-07566-y)

### Cite this article

Shumailov, I., Shumaylov, Z., Zhao, Y. _et al._ AI models collapse when trained on recursively generated data.
_Nature_ **631**, 755–759 (2024). https://doi.org/10.1038/s41586-024-07566-y

[Download citation](https://citation-needed.springer.com/v2/references/10.1038/s41586-024-07566-y?format=refman&flavour=citation)

- Received: 20 October 2023

- Accepted: 14 May 2024

- Published: 24 July 2024

- Version of record: 24 July 2024

- Issue date: 25 July 2024

- DOI: https://doi.org/10.1038/s41586-024-07566-y


### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative


Close bannerClose

![Nature Briefing AI and Robotics](https://www.nature.com/static/images/logos/nature-briefing-ai-and-robotics-logo-2a1193ada7.svg)

Sign up for the _Nature Briefing: AI and Robotics_ newsletter — what matters in AI and robotics research, free to your inbox weekly.

Email address

Sign up

I agree my information will be processed in accordance with the _Nature_ and Springer Nature Limited [Privacy Policy](https://www.nature.com/info/privacy).

Close bannerClose

Get the most important science stories of the day, free in your inbox. [Sign up for Nature Briefing: AI and Robotics](https://www.nature.com/briefing/ai-and-robotics/?brieferEntryPoint=AIAndRoboticsBriefingBanner)