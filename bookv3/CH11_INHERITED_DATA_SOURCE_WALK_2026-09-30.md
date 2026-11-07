# Chapter 11 — The education handed forward

Checked September 30, 2026. Read current Chapter 11, its prior collapse source walk, relevant literature-review entries, the archived Shumailov language procedure, and the live Gerstgrasser primary paper’s methods, ablations, outcome tables and image qualifications. Reopened *Collapse or Thrive?* to keep its fixed-budget regime separate.

## Primary record

Gerstgrasser et al., *Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data*, https://arxiv.org/html/2404.01413v2, §§2.1–2.3 and Appendices C–E.

Language models are newly initialized at each fitting iteration, rather than continuing as the same agent with a growing conversational context. TinyStories is a 470-million-token GPT-3.5/4-generated story collection. Successive generated collections replace or concatenate previous training data. Holding on to the first collection therefore does not establish a human-versus-machine source distinction: the starting language collection was already synthetic.

Appendix C/Table 2 reports, for 9M GPT-2, evaluation cross-entropy 1.82 at iteration 1; at iteration 4, 1.74 accumulation, 2.39 replacement, 2.18 growing replacement. The latter enlarges the latest model’s synthetic collection to match accumulation’s training-set size. Deterioration continues with this larger replacement set. This controls aggregate training-set size, not total generation/training pipeline compute; Appendix E explicitly distinguishes those costs. The chapter reports direction without treating cross-entropy as a proportion of factual answers.

## Outcome refinement

Language test error remains stable or improves under accumulation; molecular-conformation loss stays relatively constant. In §2.3, image accumulation slows deterioration substantially, retains major axes of variation, and generates some minor details less frequently. Appendix D shows detailed reconstructions remain possible and hypothesizes a latent-space realignment explanation. Less frequent generation is not proof that these details were erased from every representation.

The paper uses avoidance of collapse for bounded-error behavior, while its image section explicitly discusses residual deterioration. The chapter previously grouped language, molecule and image settings under one avoidance sentence. Pass 21 prints their distinct observed trajectories. Earlier reports/source walks are preserved as dated records.

Existing claim `MCL_ACCUM` previously read: “Accumulating original data and successive synthetic generations avoided collapse in the tested language, molecule, and image-model regimes.” It is updated to describe stable language/molecule loss and slowed image deterioration, linked to this correction record. The successful accumulation intervention remains central to the chapter.

## Translation and surviving argument

The workshop keeps earlier editions or replaces them with more copies of the latest one. This isolates history retained at equal page count. It does not model retrieval during deployment, nor certify the first edition as true. A growing replacement dataset supplies more descendant evidence; the accumulation archive contains earlier generations too. The measured language benefit is evaluation loss on held-out story material.

The strongest rival, “accumulation succeeds merely because its dataset is larger,” meets the growing-replacement ablation. That result supports a role for retained history in these conditions without proving every conceivable archive or selection policy will work. The later fixed-size subsampling result in https://arxiv.org/html/2410.16713 remains a separate study and outcome. No new model run or paid API call was made.
