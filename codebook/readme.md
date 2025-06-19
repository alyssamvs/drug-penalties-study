# Cocaine Policy Effectiveness Index (CPEI) - README

**Project:** Visualizing Drug Policy Effectiveness Through Data Visualization  
**Author:** 
**Institution:** Aalto University
**Thesis Program:** Art and Media - Visual Communication Design (VCD)  
**Date:** June 2025  
**Version:** 1.0

---

## 🎯 Project Overview

### **Unique Research Focus**
The Cocaine Policy Effectiveness Index (CPEI) is the first academic index to combine **cocaine-specific legal analysis** with **supply chain enforcement measurement** and **implementation reality assessment**. Unlike existing drug policy indices that focus on general drug laws, the CPEI tracks policy effectiveness from coca cultivation through street-level distribution.

### **Key Innovation: Beyond Laws on Paper**
While most drug policy research measures what laws say, the CPEI measures what countries actually do - and how well it works. This implementation-focused approach reveals the often significant gap between statutory penalties and real-world enforcement effectiveness.

### **Research Questions**
1. **Primary:** Do stricter cocaine policies lead to better enforcement outcomes?
2. **Secondary:** How do different enforcement approaches (legal vs. supply chain vs. international cooperation) compare in effectiveness?
3. **Applied:** Can data visualization of policy complexity inform better policy decisions?

---

## 🔄 Differentiation from Existing Indices

### **How CPEI Differs from Global Drug Policy Index:**

| Aspect | Global Drug Policy Index | **Cocaine Policy Effectiveness Index** |
|--------|-------------------------|----------------------------------------|
| **Scope** | All drugs, general policy | **Cocaine trafficking specific** |
| **Focus** | Legal framework only | **Supply chain + implementation** |
| **Measurement** | Laws on books | **Real-world enforcement effectiveness** |
| **Geographic** | Global coverage | **Strategic country selection** |
| **Innovation** | Policy harshness scoring | **Farm-to-table enforcement analysis** |
| **Application** | Academic comparison | **Visual communication for policy impact** |

### **Unique Contributions:**

#### **1. Cocaine-Specific Variables (★)**
- Cocaine vs. other drug penalty ratios
- Coca leaf legal status (producer countries)
- Cocaine-specific quantity thresholds
- Precursor chemical controls
- Cocaine seizure and arrest rates

#### **2. Supply Chain Analysis (★★)**
- Cultivation → Production → Transit → Distribution
- Producer/Transit/Consumer country differentiation
- Cross-border enforcement coordination
- Port/airport/maritime specific controls

#### **3. Implementation Reality (★★★)**
- Laws vs. actual sentences served
- Arrest → Prosecution → Conviction rates
- Budget allocations and resource deployment
- Operational success metrics (seizures, lab destruction)

---

## 📊 Index Structure

### **5 Dimensions, 48 Variables**

#### **Dimension 1: National Legal Framework (25%)**
- **Use & Possession Tolerance:** 12 variables
- **Trafficking Law Severity:** 8 variables
- **Focus:** Statutory foundation and penalty structure

#### **Dimension 2: Enforcement Implementation (30%)**  
- **Enforcement Intensity:** 8 variables
- **Institutional Capacity:** 4 variables
- **Focus:** Real-world enforcement effectiveness

#### **Dimension 3: International Cooperation (20%)**
- **Legal Cooperation:** 4 variables  
- **Operational Cooperation:** 4 variables
- **Focus:** Cross-border enforcement coordination

#### **Dimension 4: Supply Chain Disruption (20%)**
- **Source Control:** 4 variables
- **Transit & Distribution Control:** 4 variables  
- **Focus:** Farm-to-table enforcement approach

#### **Dimension 5: Harm Reduction Balance (5%)**
- **Treatment Integration:** 4 variables
- **Focus:** Policy approach balance indicator

---

## 🗺️ Country Coverage & Selection

### **Strategic Sample: 12 Countries**

#### **Producer Countries (3)**
- **Peru:** Constitutional coca rights + eradication programs
- **Colombia:** Comprehensive supply chain enforcement  
- **Bolivia:** Legal coca + limited eradication

#### **Transit Countries (4)**
- **Spain:** Major European entry point (ports)
- **Netherlands:** Port of Rotterdam cocaine hub
- **France:** Transit and consumption center
- **Belgium:** Port of Antwerp cocaine focus

#### **Consumer Countries (5)**
- **USA:** Comprehensive prohibition approach
- **Sweden:** Zero tolerance policy model
- **Portugal:** Decriminalization + treatment focus
- **Greece:** High penalties, enforcement focus
- **Finland:** Nordic harm reduction model

**Selection Rationale:** Covers full supply chain (source → transit → destination) with diverse policy approaches for meaningful comparison.

---

## 📈 Calculation Methodology

### **Composite Index Formula:**
```
CPEI = (Legal_Framework × 0.25) + (Enforcement × 0.30) + 
       (International × 0.20) + (Supply_Chain × 0.20) + (Harm_Reduction × 0.05)
```

### **Scoring Approach:**
- **Binary Variables:** 1=Strict, 0=Liberal, 0.5=Mixed/Unclear
- **Continuous Variables:** Normalized to 0-1 scale  
- **Ordinal Variables:** Scaled to 0, 0.5, or 1
- **Missing Data:** Conservative scoring with quality flags

### **Weighting Rationale:**
- **Enforcement (30%):** Implementation matters more than laws
- **Legal Framework (25%):** Necessary foundation
- **International (20%):** Critical for transnational trafficking
- **Supply Chain (20%):** Your unique innovation
- **Harm Reduction (5%):** Policy balance indicator

---

## 📋 Data Collection Guide

### **Priority Collection Order:**

#### **Phase 1: Core Differentiation (Weeks 1-2)**
**High-impact, cocaine-specific variables:**
- LEG_USE_04: Cocaine-specific possession thresholds
- LEG_USE_05: Cocaine vs. other drug penalty ratios  
- LEG_USE_10: Coca leaf legal status
- LEG_SUP_08: Cocaine precursor controls
- SUP_SRC_01: Coca cultivation controls

#### **Phase 2: Implementation Measures (Weeks 3-4)**
**Real-world enforcement effectiveness:**
- ENF_INT_01-08: Arrest, prosecution, conviction rates
- ENF_INT_03: Average sentences actually served
- ENF_INT_06: Drug enforcement budgets
- ENF_INT_08: Cocaine seizure rates

#### **Phase 3: International & Supply Chain (Weeks 5-6)**
**Cross-border and supply chain variables:**
- INT_OPS_01-04: DEA/Europol cooperation
- SUP_TRN_01-04: Lab destruction, port security
- INT_LEG_01-04: Extradition, legal cooperation

### **Data Quality Standards:**
| Quality Level | Action | Coding |
|---------------|---------|---------|
| **High Quality (HQ)** | Multiple government sources | Standard scoring |
| **Medium Quality (MQ)** | Single reliable source | Standard scoring + note |
| **Low Quality (LQ)** | Contradictory sources | Conservative scoring (0.5) |
| **No Data (ND)** | No reliable source | Conservative scoring + flag |

---

## 📊 Expected Results & Analysis

### **Hypothesis Testing:**
1. **Legal strictness ≠ enforcement effectiveness**
2. **Supply chain coordination > isolated national policies**
3. **International cooperation > unilateral enforcement**  
4. **Implementation gaps largest in high-penalty countries**

### **Country Profile Predictions:**

#### **USA:** High Legal + High Enforcement + Mixed Outcomes
- Prediction: High legal scores, high enforcement resources, but implementation gaps in supply chain coordination

#### **Netherlands:** Moderate Legal + High International + Effective Outcomes  
- Prediction: Lower legal strictness but high international cooperation and port security effectiveness

#### **Colombia:** High Supply Chain + High International + Producer Challenges
- Prediction: Comprehensive supply chain enforcement but persistent cultivation challenges

#### **Portugal:** Low Legal + High Harm Reduction + Health Outcomes
- Prediction: Lowest legal strictness but high treatment integration and health outcomes

---

## 🔧 File Structure

```
cocaine-policy-index/
├── README.md                          # This file
├── codebook_variables.csv             # Variable documentation (48 variables)
├── data/
│   ├── raw_data.xlsx                  # Country data collection
│   ├── calculated_scores.xlsx         # Computed dimension scores
│   └── final_index.csv                # CPEI results and rankings
├── methodology/
│   ├── calculation_guide.md           # Step-by-step formulas
│   ├── data_sources.md                # Source documentation
│   └── validation_results.md          # Quality assurance outcomes
├── visualizations/
│   ├── index_dashboard.html           # Interactive results dashboard
│   ├── country_profiles.html          # Individual country analysis
│   ├── supply_chain_maps.html         # Geographic enforcement visualization
│   └── correlation_analysis.png       # Policy effectiveness relationships
└── thesis_integration/
    ├── methodology_chapter.md         # Thesis methodology section
    ├── results_chapter.md             # Results and analysis
    └── policy_implications.md         # Policy recommendations
```

---

## 📚 Key Data Sources

### **Primary Sources (Hierarchical Priority):**

#### **1. Government Legislation & Implementation**
- National criminal codes and penal legislation
- Drug control laws and scheduling regulations
- Law enforcement budgets and resource allocation
- Prison statistics and corrections data

#### **2. International Organizations**
- **UNODC:** World Drug Report, country profiles, seizure data
- **INCB:** Precursor control assessments, compliance reports
- **EUDA:** European drug enforcement statistics, sentencing data
- **DEA:** International cooperation reports, operation statistics

#### **3. Specialized Enforcement Agencies**
- National police drug enforcement units
- Customs and border control agencies  
- Coast guard and maritime interdiction
- Financial intelligence units

#### **4. Academic & Research Sources**
- Peer-reviewed drug policy effectiveness research
- University drug policy center reports
- Independent policy analysis (Transform, Drug Policy Alliance)

### **Source Validation Protocol:**
- **Cross-referencing:** Minimum 2 independent sources per critical variable
- **Currency verification:** Data within 24 months of collection
- **Translation validation:** Professional translation for non-English sources
- **Expert consultation:** Local drug policy expert review when possible

---

## ✅ Quality Assurance

### **Validation Procedures:**

#### **Face Validity**
- Expert review by drug policy researchers
- Ranking validation against known policy approaches
- Component score logical consistency analysis

#### **Content Validity**  
- Literature review of cocaine policy dimensions
- Stakeholder feedback from law enforcement experts
- Comparison with existing policy measurement frameworks

#### **Construct Validity**
- Factor analysis of variable clustering
- Convergent validity with related measures
- Discriminant validity between policy approaches

#### **Reliability Testing**
- Inter-rater reliability for subjective coding
- Test-retest consistency over time periods
- Internal consistency analysis (Cronbach's alpha)

### **Sensitivity Analysis:**
1. **Alternative weighting schemes** (equal weights, expert-derived weights)
2. **Variable exclusion impact** (removing individual indicators)
3. **Missing data handling** (different imputation methods)
4. **Outlier country impact** (influence of extreme cases)

---

## 🎨 Visual Communication Integration

### **Thesis Application - Visual Communication Design:**

#### **Interactive Dashboard Features:**
- **Country comparison radar charts** (5-dimension profiles)
- **Supply chain flow maps** (cultivation → consumption visualization)
- **Implementation gap analysis** (laws vs. reality scatter plots)
- **Correlation matrix** (policy dimensions vs. outcomes)

#### **Policy Story Visualization:**
- **Scrolly-tell narrative** progressing through supply chain stages
- **Country case studies** with visual policy profiles  
- **Effectiveness correlation** between strictness and outcomes
- **Policy recommendation** framework based on successful approaches

#### **Design Innovation:**
- **Interactive policy exploration** allowing users to adjust weights
- **Geographic enforcement visualization** showing cross-border cooperation
- **Temporal policy tracking** (future expansion for policy changes)

---

## 📊 Applications & Impact

### **Academic Applications:**
- **Comparative drug policy research** with cocaine-specific focus
- **Policy effectiveness analysis** linking approaches to outcomes
- **International relations** in drug enforcement cooperation
- **Criminology research** on enforcement strategy effectiveness

### **Policy Applications:**
- **International benchmarking** for government policy review
- **Evidence-based reform** advocacy with quantified comparisons
- **Resource allocation** decisions informed by effectiveness data
- **International cooperation** planning and priority setting

### **Visual Communication Applications:**
- **Policy advocacy** with clear, compelling data visualization
- **Public education** about drug policy complexity and effectiveness
- **Policymaker briefings** with actionable comparative insights
- **Academic presentation** of complex policy relationships

---

## 📖 Citation & Attribution

### **Academic Citation (APA Style):**
```
[Your Name]. (2025). Cocaine Policy Effectiveness Index: A Visual Analysis of 
Supply Chain Enforcement Approaches [Unpublished master's thesis]. [Your Institution].
```

### **Dataset Citation:**
```
[Your Name]. (2025). Cocaine Policy Effectiveness Index Dataset (Version 1.0) [Data set]. 
[Repository URL when available]
```

### **Recommended Attribution:**
When using this index, methodology, or data:
- Cite original research and methodology
- Acknowledge cocaine-specific focus and innovation
- Reference supply chain analysis framework
- Credit visual communication design application
- Note version and limitations

---

## 🔮 Future Development

### **Version 2.0 Planned Enhancements:**
- **Temporal analysis:** Multi-year policy change tracking
- **Outcome correlation:** Link to drug availability, health outcomes
- **Additional countries:** Expand to 20+ strategic countries
- **Micro-analysis:** Subnational policy variation (federal systems)

### **Research Applications:**
- **Longitudinal studies:** Track policy effectiveness over time
- **Natural experiments:** Analyze policy reform impacts
- **Causal analysis:** Identify most effective enforcement combinations
- **Predictive modeling:** Forecast policy outcome probabilities

### **Visual Communication Expansion:**
- **Real-time dashboard:** Live policy tracking and updates
- **Policy simulation tool:** "What if" scenario modeling
- **Mobile application:** Accessible policy comparison tool
- **VR visualization:** Immersive supply chain enforcement experience

---

## 📞 Contact & Collaboration

**Primary Researcher:** [Your Name]  
**Email:** [your.email@institution.edu]  
**Institution:** [Your Institution]  
**Department:** Art and Media - Visual Communication Design  
**Thesis Advisor:** [Advisor Name]

**Collaboration Opportunities:**
- **Academic partnerships:** Drug policy research collaboration
- **Policy consultation:** Government and NGO advisory work
- **Data sharing:** Contributing to broader drug policy research
- **Visual design:** Policy visualization and communication projects

**Project Repository:** [GitHub URL when available]  
**Interactive Dashboard:** [Website URL when available]

---

## ⚖️ License & Terms

This work is licensed under Creative Commons Attribution 4.0 International License.

**You are free to:**
- **Share:** Copy and redistribute the material in any medium or format
- **Adapt:** Remix, transform, and build upon the material for any purpose

**Under the following terms:**
- **Attribution:** Provide appropriate credit, citation, and indicate if changes were made
- **Academic integrity:** Maintain research standards and acknowledge sources
- **Policy application:** Encourage evidence-based policy development

---

## 🙏 Acknowledgments

- **Thesis Advisor:** [Advisor Name] - Methodology guidance and research direction
- **Expert Consultations:** [Names] - Drug policy expertise and validation
- **Data Collection Support:** [Names] - Research assistance and source access
- **Technical Support:** [Names] - Data analysis and visualization development
- **Funding Support:** [Sources] - Research and development funding

---

## 📝 Version History

| Version | Date | Major Changes | Focus |
|---------|------|---------------|-------|
| 0.1 | [Date] | Initial concept and literature review | Research design |
| 0.5 | [Date] | Pilot data collection and methodology | Framework development |
| 1.0 | June 2025 | Full index implementation | Current version |
| 1.1 | [Planned] | Expert validation and refinements | Quality assurance |
| 2.0 | [Future] | Temporal analysis and expansion | Longitudinal research |

---

*"The most effective drug policies may not be the harshest ones. Through data visualization of enforcement reality, we can reveal what works - and what doesn't - in the complex world of cocaine policy."*

---

**Last Updated:** [Date]  
**README Version:** 1.0  
**Project Status:** Active Development