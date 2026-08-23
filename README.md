<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0969da,100:54aeff&height=200&section=header&text=Mrityunjay%20Singh&fontSize=60&animation=fadeIn&fontColor=ffffff&fontAlignY=36&desc=AI%20Systems%20Engineer%20%7C%20Behavioural%20Modelling%20%7C%20Causal%20Design&descAlignY=58&descAlign=50" width="100%"/>
</div>

<div align="center">

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=22&pause=1200&color=58a6ff&center=true&vCenter=true&width=650&height=50&lines=First-named+inventor+on+filed+provisional+patent.;LLM+Distillation+%E2%80%A2+Causal+Intervention+Design.;Verification+over+generation+%E2%80%A2+Spec-first+development." alt="Typing SVG" />
</a>

<br/>

[![GitHub followers](https://img.shields.io/github/followers/yamantaka-singh?label=Follow&style=social)](https://github.com/yamantaka-singh)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-1e1e1e?style=for-the-badge&logo=linkedin&logoColor=58a6ff)](https://linkedin.com/in/yamantakasingh)
[![HackerRank](https://img.shields.io/badge/HackerRank-1e1e1e?style=for-the-badge&logo=hackerrank&logoColor=58a6ff)](https://hackerrank.com/profile/25bai70030)
[![Email](https://img.shields.io/badge/Email-1e1e1e?style=for-the-badge&logo=gmail&logoColor=58a6ff)](mailto:mrityunjaysinght2005@gmail.com)

</div>

---

### 👤 Executive Summary

> **Second-year B.E. (Hons.) Computer Science (AI & ML) student at Chandigarh University.** 
> First-named inventor on a filed provisional patent (`IN202611015895`) for real-time cognitive state estimation from behavioural telemetry, and lead author of the systems paper behind it. Specializes in end-to-end research engineering: LLM distillation into from-scratch regressors with popularity blindfolds, causal RCT protocol design, and deterministic verification harnesses.

---

### 💻 Featured Systems & Engineering Projects

#### 🌐 [GitGlobe — Semantic Map of the Open-Source Ecosystem](https://github.com/yamantaka-singh/GitGlobe)
`Python` · `PostgreSQL` · `NumPy` · `TypeScript` · `WebGL` · `NVIDIA NIM`

- **LLM → Model Distillation with Popularity Blindfold**: NVIDIA Nemotron 550B (via NIM) rates a stratified sample of repositories against a 6-dimension quality rubric; a gradient-boosted tree regressor written from scratch in NumPy (histogram splitting, level-wise trees, early stopping) distils those judgements to all 95,384 rows. Star and fork counts are stripped from both the teacher prompt and student features, enforced by automated tests to prevent the model from simply learning popularity.
- **Strict Validation Bar**: Refused to ship a model that had not earned it. A dimension is stored only if its held-out RMSE beats the mean-predictor by more than sampling noise ($\text{baseline}/\sqrt{2n}$). Four of six dimensions passed at $R^2 = 0.21\text{--}0.44$.
- **Empirical Star Survival Function**: Measured GitHub's star survival function across a 29-rung ladder (~322M repositories) instead of assuming a power law, diagnosing that in-corpus percentiles were saturated at $0.998\text{--}1.000$ and ordering nothing.
- **High-Performance Spatial Systems**: Custom binary tile format (12 bytes/point, 3 LOD bands, 3.2 MB for 87,227 nodes); 234,640-entry CSR graph with PageRank; UMAP 3-D projection and spherical k-means clustering; WebGL renderer with GPU picking. 446 tests across 19 suites enforcing NASA Power-of-10 rules.

#### 🛡️ [unlearn-shield — Machine Unlearning for Tabular Fraud Models](https://github.com/yamantaka-singh/unlearn-shield)
`Python` · `Machine Unlearning` · `SISA Architecture` · `Cryptographic Manifests` · `Determinism`

- **Targeted Erasure without Full Retraining**: Implements SISA (Sharded, Isolated, Sliced, Aggregated) architecture for exact and certified data unlearning in high-throughput tabular fraud detection pipelines.
- **Signed Auditability**: Generates cryptographic erasure manifests with sha256 lineage tracking to provide mathematically verifiable guarantees for "Right-to-be-Forgotten" compliance.
- **Determinism Harness**: Strict test harness verifying bit-level reproducibility and isolating delta updates across model slice boundaries.

#### 🧠 Project S.A.G.E. — Behavioural Telemetry → Latent Cognitive State
`Passive Telemetry` · `Causal Inference` · `Sensor Fusion` · `SaMD Protocol`

- **Passive Interaction Telemetry**: Designed non-invasive instruments that infer latent executive-function states purely from interaction signals (time-to-click against word count, scroll velocity, cursor trajectory, keystroke flight-time deviation) with decision thresholds derived from reading-speed norms.
- **Causal RCT Protocol ($N = 240$)**: Authored a pre-registered multicentre randomised controlled trial protocol (1:1 stratified randomisation, assessor-blinded) and statistical analysis plan: power justification, ITT/PP populations, multiplicity control, and interim analysis.
- **Deployment & Governance**: Regulatory strategy across a dual wellness/SaMD track, threat model, interface control specifications, and CI/CD with automated SBOM generation and SLSA provenance.

---

### 🔬 Research & Intellectual Property

- 📜 **Provisional Patent (First-Named Inventor)**
  - **Title**: *Real-Time Cognitive State Estimation & Environmental Modulation*
  - **Filing**: Indian Patent Office · App. No. `IN202611015895` · Filed 12 February 2026 (Project S.A.G.E.)
  - **Architecture**: Hardware-agnostic cognitive digital twin via multi-modal sensor fusion and closed-loop feedback, keyed to quantifiable signal variances rather than abstract psychometric traits.
  - **Governance**: Consent-bounded, fail-safe intervention protocols with pre-authorised modulation thresholds.

- 📝 **Lead Author — Systems Paper**
  - **Title**: *"Cognitive Architecture and Stochastic Algorithmic Reinforcement: A Systems Model of Adolescent Vulnerability"*
  - **Authors**: Singh, Dabas & Kanan (2026)
  - **Mechanistic Scope**: Modelled how variable-ratio reinforcement schedules in recommendation engines interact with delayed prefrontal maturation to shift users toward fast associative processing.
  - **Remediation Framework**: Proposed a two-vector remedy pairing a fiduciary duty-of-care standard with deterministic pre-commitment interfaces grounded in dual-process theory.

---

### ⚙️ Engineering Discipline & How I Build

```yaml
engineering_discipline:
  verification_over_generation: "Agent & model output is assumed wrong until measured against held-out ground truth."
  tests_as_specification: "Every guard is tested for its ability to fail; checks that cannot fail are decoration."
  spec_first_execution: "Architecture decision records (ADRs) and formal plans precede code execution."
  research_rigor: "Literature synthesis with load-bearing claims verified against primary empirical sources."
```

---

### 🛠️ Technical Arsenal

<table>
  <tr>
    <td align="center" width="22%"><b>Languages</b></td>
    <td>
      <img src="https://img.shields.io/badge/Python-1e1e1e?style=flat-square&logo=python&logoColor=58a6ff" />
      <img src="https://img.shields.io/badge/C++-1e1e1e?style=flat-square&logo=c%2B%2B&logoColor=58a6ff" />
      <img src="https://img.shields.io/badge/TypeScript-1e1e1e?style=flat-square&logo=typescript&logoColor=58a6ff" />
      <img src="https://img.shields.io/badge/C-1e1e1e?style=flat-square&logo=c&logoColor=58a6ff" />
      <img src="https://img.shields.io/badge/SQL-1e1e1e?style=flat-square&logo=postgresql&logoColor=58a6ff" />
      <img src="https://img.shields.io/badge/GLSL-1e1e1e?style=flat-square&logo=opengl&logoColor=58a6ff" />
      <img src="https://img.shields.io/badge/HTML5%2FCSS3-1e1e1e?style=flat-square&logo=html5&logoColor=58a6ff" />
    </td>
  </tr>
  <tr>
    <td align="center" width="22%"><b>ML & Distillation</b></td>
    <td>
      <img src="https://img.shields.io/badge/PyTorch-1e1e1e?style=flat-square&logo=pytorch&logoColor=58a6ff" />
      <img src="https://img.shields.io/badge/NumPy-1e1e1e?style=flat-square&logo=numpy&logoColor=58a6ff" />
      <img src="https://img.shields.io/badge/scikit--learn-1e1e1e?style=flat-square&logo=scikit-learn&logoColor=58a6ff" />
      <img src="https://img.shields.io/badge/Knowledge_Distillation-1e1e1e?style=flat-square" />
      <img src="https://img.shields.io/badge/Machine_Unlearning_(SISA)-1e1e1e?style=flat-square" />
      <img src="https://img.shields.io/badge/UMAP%20%26%20HDBSCAN-1e1e1e?style=flat-square" />
      <img src="https://img.shields.io/badge/PageRank-1e1e1e?style=flat-square" />
      <img src="https://img.shields.io/badge/Vertex_AI_Embeddings-1e1e1e?style=flat-square&logo=google-cloud&logoColor=58a6ff" />
    </td>
  </tr>
  <tr>
    <td align="center" width="22%"><b>LLM & Agent Systems</b></td>
    <td>
      <img src="https://img.shields.io/badge/Structured_Outputs-1e1e1e?style=flat-square" />
      <img src="https://img.shields.io/badge/Rubric_Design-1e1e1e?style=flat-square" />
      <img src="https://img.shields.io/badge/Data_Leakage_Guards-1e1e1e?style=flat-square" />
      <img src="https://img.shields.io/badge/Teacher--Student_Distillation-1e1e1e?style=flat-square" />
      <img src="https://img.shields.io/badge/Agentic_CI%2FCD-1e1e1e?style=flat-square" />
    </td>
  </tr>
  <tr>
    <td align="center" width="22%"><b>Causal & Quantitative</b></td>
    <td>
      <img src="https://img.shields.io/badge/RCT_Protocol_Design-1e1e1e?style=flat-square" />
      <img src="https://img.shields.io/badge/Statistical_Analysis_Planning-1e1e1e?style=flat-square" />
      <img src="https://img.shields.io/badge/Power_Analysis-1e1e1e?style=flat-square" />
      <img src="https://img.shields.io/badge/Difference--in--Differences-1e1e1e?style=flat-square" />
      <img src="https://img.shields.io/badge/Propensity_Scoring-1e1e1e?style=flat-square" />
    </td>
  </tr>
  <tr>
    <td align="center" width="22%"><b>Infra & Cloud</b></td>
    <td>
      <img src="https://img.shields.io/badge/PostgreSQL-1e1e1e?style=flat-square&logo=postgresql&logoColor=58a6ff" />
      <img src="https://img.shields.io/badge/Google_Cloud%20(BigQuery%2C%20Vertex)-1e1e1e?style=flat-square&logo=google-cloud&logoColor=58a6ff" />
      <img src="https://img.shields.io/badge/WebGL-1e1e1e?style=flat-square&logo=webgl&logoColor=58a6ff" />
      <img src="https://img.shields.io/badge/Git%20%26%20GitHub_Actions-1e1e1e?style=flat-square&logo=github&logoColor=58a6ff" />
      <img src="https://img.shields.io/badge/SBOM%20%26%20SLSA_Provenance-1e1e1e?style=flat-square" />
    </td>
  </tr>
</table>

---

<div align="center">
  <h3>🏙️ 3D Contribution Landscape</h3>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yamantaka-singh/yamantaka-singh/main/profile-3d-contrib/profile-night-view.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/yamantaka-singh/yamantaka-singh/main/profile-3d-contrib/profile-night-view.svg">
    <img alt="3D Github Contribution Graph" src="https://raw.githubusercontent.com/yamantaka-singh/yamantaka-singh/main/profile-3d-contrib/profile-night-view.svg" width="100%">
  </picture>
</div>

<br/>

<div align="center">
  <h3>📊 Verified Engineering Activity & Metrics</h3>
  <img src="github-metrics.svg" alt="GitHub Metrics" width="95%" />
</div>

<br/>

<div align="center">
  <h3>🐍 Dynamic Contribution Simulation</h3>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yamantaka-singh/yamantaka-singh/output/github-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/yamantaka-singh/yamantaka-singh/output/github-snake.svg">
    <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/yamantaka-singh/yamantaka-singh/output/github-snake.svg" width="100%">
  </picture>
</div>

---

<div align="center">
  <sub>Engineered with precision • Spec-first & Agent-executed • © 2026 Mrityunjay Singh</sub>
</div>
