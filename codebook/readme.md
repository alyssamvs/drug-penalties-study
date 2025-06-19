# Drug Policy Strictness Index - README

**Project:** Visualizing Drug Policy Effectiveness Through Data Visualization  
**Author:** [Your Name]  
**Institution:** [Your Institution]  
**Date:** June 2025  
**Version:** 2.0 (Supply Chain Enhanced)

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Quick Start](#quick-start)
3. [File Structure](#file-structure)
4. [Index Methodology](#index-methodology)
5. [Data Collection Guide](#data-collection-guide)
6. [Calculation Instructions](#calculation-instructions)
7. [Results Interpretation](#results-interpretation)
8. [Data Sources](#data-sources)
9. [Quality Assurance](#quality-assurance)
10. [Troubleshooting](#troubleshooting)
11. [Citation](#citation)
12. [Contact](#contact)

---

## 🎯 Project Overview

### Purpose
The Drug Policy Strictness Index (DPSI) quantifies and compares the relative harshness of cocaine-related drug policies across countries. This index combines legal framework analysis with supply chain enforcement assessment to provide a comprehensive measure of policy approach and effectiveness.

### Research Question
**"Do stricter drug policies lead to better outcomes in cocaine trafficking control?"**

### Key Innovation
Unlike existing drug policy indices that focus solely on legal penalties, the DPSI incorporates **supply chain enforcement** measures, tracking policy implementation from cultivation through distribution.

### Scope
- **Geographic Coverage:** 12 countries across Europe, Americas, and Oceania
- **Temporal Coverage:** Current legal frameworks and enforcement practices (2024-2025)
- **Drug Focus:** Cocaine trafficking, possession, and use
- **Policy Dimensions:** Legal framework + Supply chain enforcement

---

## 🚀 Quick Start

### Prerequisites
- Excel or CSV-compatible software
- Basic understanding of drug policy terminology
- Access to government databases and reports

### Basic Usage
1. **Open the codebook:** `codebook_variables.csv`
2. **Review the data:** `12countrieslegaldata.xlsx`
3. **Calculate index:** Use the formulas in Section 6
4. **Interpret results:** Rankings from 0 (most liberal) to 1 (most strict)

### Current Results Summary
| Rank | Country | Index Score | Policy Approach |
|------|---------|-------------|-----------------|
| 1 | USA | 0.76 | Comprehensive Strictness |
| 2 | Colombia | 0.72 | Producer Country Enforcement |
| 3 | Peru | 0.70 | Mixed Approach |
| ... | ... | ... | ... |
| 12 | Netherlands | 0.36 | Liberal/Harm Reduction |

---

## 📁 File Structure

```
drug-policy-index/
├── README.md                           # This file
├── codebook_variables.csv              # Variable documentation
├── 12countrieslegaldata.xlsx          # Raw data collection
├── index_calculations.xlsx             # Computed scores
├── methodology/
│   ├── calculation_guide.pdf          # Step-by-step formulas
│   ├── data_sources.md                # Source documentation
│   └── quality_checks.md              # Validation procedures
├── visualizations/
│   ├── index_dashboard.html           # Interactive results
│   ├── country_profiles.html          # Individual country analysis
│   └── correlation_plots.png          # Policy vs outcomes
└── expansion/
    ├── supply_chain_variables.csv     # Additional variables for v2.0
    └── collection_templates.xlsx      # Data gathering templates
```

---

## 🔬 Index Methodology

### Conceptual Framework
The DPSI measures policy strictness across five dimensions:

1. **USE (5% weight):** Criminalization of drug use
2. **POSSESSION (20% weight):** Penalties for drug possession
3. **SUPPLY (30% weight):** Trafficking and distribution laws
4. **SENTENCES (15% weight):** Actual penalty severity
5. **SUPPLY_CHAIN (30% weight):** Enforcement across trafficking stages

### Version History
- **v1.0:** Basic legal framework analysis (28 variables)
- **v2.0:** Added supply chain enforcement (38 variables) ← Current

### Scoring Methodology
- **Binary variables:** Yes=1, No=0, Unclear=0.5
- **Continuous variables:** Normalized to 0-1 scale
- **Ordinal variables:** Scaled to 0, 0.5, or 1
- **Missing data:** Conservative scoring (0.5 for binary, 0 for continuous)

### Composite Calculation
```
DPSI = (USE × 0.05) + (POSSESSION × 0.20) + (SUPPLY × 0.30) + 
       (SENTENCES × 0.15) + (SUPPLY_CHAIN × 0.30)
```

---

## 📊 Data Collection Guide

### Phase 1: Legal Framework (Complete)
**Status:** ✅ Complete for all 12 countries  
**Variables:** 28  
**Sources:** Government legislation, penal codes, sentencing guidelines

### Phase 2: Supply Chain Enforcement (In Progress)
**Status:** 🔄 Current expansion focus  
**Variables:** 10 additional  
**Priority Order:**
1. Coca legal status (producer countries)
2. Organized crime laws (all countries)
3. Precursor chemical controls (all countries)
4. Port/airport security measures
5. Border enforcement programs

### Country Categories
**Producer Countries:** Peru, Colombia, Bolivia
- Focus: Cultivation control, eradication programs, alternative development

**Transit Countries:** Spain, France, Netherlands, Belgium
- Focus: Border security, port controls, transit monitoring

**Consumer Countries:** USA, Sweden, Greece, Portugal, Brazil
- Focus: Organized crime laws, demand reduction, treatment programs

### Data Quality Standards
| Quality Level | Criteria | Action |
|---------------|----------|---------|
| **High (HQ)** | Multiple verified government sources | Use standard scoring |
| **Medium (MQ)** | Single reliable official source | Use standard scoring, note limitation |
| **Low (LQ)** | Contradictory or unclear sources | Use conservative scoring (0.5) |
| **No Data (ND)** | No reliable source found | Use conservative scoring, flag for future |

---

## 🧮 Calculation Instructions

### Step 1: Data Preparation
1. Open `12countrieslegaldata.xlsx`
2. Verify all data is properly formatted
3. Check for missing values and apply conservative scoring rules

### Step 2: Category Score Calculation

#### USE Category (5% weight)
```
USE_SCORE = (Use_Criminal_Offense + Use_Admin_Offense) / 2
```

#### POSSESSION Category (20% weight)
```
POSSESSION_SCORE = (Possession_Criminal + Possession_Admin + Prison_Possible + 
                   Penalty_Quantity + Penalty_Recidivism + Threshold_Amounts) / 6
```

#### SUPPLY Category (30% weight)
```
SUPPLY_SCORE = (Supply_Threshold + Mandatory_Minimums + Supply_Penalty_Quantity + 
                Supply_Penalty_Recidivism + Special_Measures) / 5
```

#### SENTENCES Category (15% weight)
```
Max_Possession_Norm = min(Max_Possession_Years / 10, 1.0)
Max_Supply_Norm = min(Max_Supply_Years / 40, 1.0)
Min_Supply_Norm = min(Min_Supply_Years / 20, 1.0)

SENTENCES_SCORE = (Max_Possession_Norm + Max_Supply_Norm + Min_Supply_Norm) / 3
```

#### SUPPLY_CHAIN Category (30% weight)
```
SUPPLY_CHAIN_SCORE = (Coca_Legal_Status + Eradication_Programs + Alternative_Development + 
                      Precursor_Controls + Border_Enforcement + Port_Security + 
                      Organized_Crime_Laws + Transit_Monitoring) / 8
```

### Step 3: Composite Index
```
DPSI = (USE_SCORE × 0.05) + (POSSESSION_SCORE × 0.20) + (SUPPLY_SCORE × 0.30) + 
       (SENTENCES_SCORE × 0.15) + (SUPPLY_CHAIN_SCORE × 0.30)
```

### Step 4: Ranking
Sort countries by DPSI score (descending) and assign ranks 1-12.

---

## 📈 Results Interpretation

### Score Ranges
- **0.75-1.00:** Very Strict (Comprehensive prohibition approach)
- **0.50-0.74:** Moderately Strict (Balanced enforcement)
- **0.25-0.49:** Moderately Liberal (Treatment-focused)
- **0.00-0.24:** Very Liberal (Decriminalization approach)

### Policy Typology
**Based on component scores, countries can be classified as:**

1. **Comprehensive Prohibition:** High legal + High supply chain (e.g., USA)
2. **Producer Country Enforcement:** High supply chain + Moderate legal (e.g., Colombia)
3. **Transit Country Focus:** High supply chain + Low legal (e.g., Netherlands ports)
4. **Consumer Country Treatment:** Low supply chain + Moderate legal (e.g., Portugal)
5. **Liberal Approach:** Low across all dimensions (e.g., Netherlands general)

### Statistical Significance
- **Difference < 0.05:** Not meaningfully different
- **Difference 0.05-0.10:** Potentially meaningful difference
- **Difference > 0.10:** Clear policy difference
- **Difference > 0.20:** Fundamental approach difference

---

## 📚 Data Sources

### Primary Sources (Hierarchical Priority)
1. **Government Legislation**
   - National penal codes and criminal law
   - Drug control legislation and regulations
   - Sentencing guidelines and judicial procedures

2. **International Organizations**
   - UNODC World Drug Report and country profiles
   - INCB (International Narcotics Control Board) reports
   - EUDA (European Union Drugs Agency) enforcement data

3. **Law Enforcement Agencies**
   - National police annual reports
   - Customs and border control statistics
   - Specialized drug enforcement unit reports

4. **Academic and Research Institutions**
   - Peer-reviewed drug policy research
   - University drug policy center reports
   - Independent policy analysis organizations

### Source Verification
- **Cross-referencing:** Minimum 2 independent sources per indicator
- **Currency:** Data within 2 years of collection date
- **Translation:** Professional translation for non-English sources
- **Expert consultation:** Local drug policy expert review where possible

### Specific Source Examples
| Variable Type | Example Sources |
|---------------|-----------------|
| Legal Framework | France: Code Pénal, Article 222-34 to 222-39 |
| Sentencing Data | EUDA Drug Offences Report 2024 |
| Supply Chain | Colombia: National Police Counter-Narcotics Report |
| Budget Data | US: DEA Congressional Budget Justification |
| International | Europol: EU Drug Markets Report |

---

## ✅ Quality Assurance

### Validation Procedures

#### Face Validity
- **Expert Review:** Index shared with drug policy researchers
- **Ranking Validation:** Do results align with expert knowledge?
- **Component Analysis:** Do high-scoring categories correlate logically?

#### Content Validity
- **Literature Review:** Do indicators cover all relevant policy dimensions?
- **Stakeholder Input:** Feedback from law enforcement and policy experts
- **International Comparison:** Alignment with existing policy measures

#### Construct Validity
- **Factor Analysis:** Do indicators cluster as expected?
- **Correlation Analysis:** Relationship between index components
- **Discriminant Validity:** Can index distinguish between policy approaches?

#### Reliability Testing
- **Inter-rater Reliability:** Multiple coders score subset of countries
- **Test-retest Reliability:** Consistency over time periods
- **Internal Consistency:** Cronbach's alpha for scale reliability

### Sensitivity Analysis
1. **Alternative Weighting:** Test different category weights
2. **Indicator Exclusion:** Remove individual indicators to test robustness
3. **Missing Data Methods:** Compare different imputation approaches
4. **Outlier Analysis:** Impact of extreme values on rankings

### Error Checking
- **Data Entry Validation:** Double-entry verification for critical variables
- **Calculation Verification:** Independent calculation of index scores
- **Logic Checks:** Impossible value combinations flagged
- **Temporal Consistency:** Changes over time period plausible

---

## 🔧 Troubleshooting

### Common Issues

#### Problem: Missing Data for Specific Countries
**Solution:** 
- Use conservative scoring (0.5 for binary, 0 for continuous)
- Document missing data in quality flags
- Prioritize data collection for high-impact variables

#### Problem: Inconsistent Source Information
**Solution:**
- Use hierarchical source priority (government > international > academic)
- Document conflicting information in notes
- Consult local experts when possible

#### Problem: Index Rankings Don't Match Expectations
**Solution:**
- Review component scores to identify drivers
- Validate data collection for surprising cases
- Consider alternative weighting schemes
- Document and investigate anomalies

#### Problem: Data Collection Taking Too Long
**Solution:**
- Focus on high-weight variables first
- Use proxy measures when exact data unavailable
- Set realistic timelines for data availability
- Consider reducing scope if necessary

### Technical Issues

#### Excel Formula Errors
- Check cell references and ensure proper range selection
- Verify data types (numbers vs text)
- Use absolute references ($A$1) for constants

#### Data Import Problems
- Ensure CSV files use UTF-8 encoding
- Check for hidden characters or formatting issues
- Verify column headers match codebook exactly

---

## 🏆 Applications

### Academic Uses
- **Comparative drug policy research**
- **Policy effectiveness analysis**
- **International relations studies**
- **Criminology and criminal justice research**

### Policy Applications
- **International benchmarking**
- **Policy reform advocacy**
- **Resource allocation decisions**
- **International cooperation planning**

### Visualization Opportunities
- **Country comparison dashboards**
- **Policy dimension radar charts**
- **Correlation with outcome measures**
- **Time series analysis (future versions)**

---

## 📖 Citation

### Academic Citation (APA Style)
```
[Your Name]. (2025). Drug Policy Strictness Index: A Comparative Analysis of Cocaine 
Enforcement Approaches [Unpublished master's thesis]. [Your Institution].
```

### Dataset Citation
```
[Your Name]. (2025). Drug Policy Strictness Index Dataset (Version 2.0) [Data set]. 
https://github.com/[your-username]/drug-policy-index
```

### Recommended Attribution
When using this index or methodology, please cite the original work and acknowledge:
- Data collection methodology
- Index calculation procedures
- Limitations and assumptions
- Version number used

---

## 🔮 Future Development

### Planned Enhancements (v3.0+)
- **Temporal Analysis:** Multi-year data collection
- **Additional Countries:** Expand to 20+ countries
- **Implementation Measures:** Enforcement budgets and personnel
- **Outcome Correlation:** Link to drug availability and health outcomes

### Potential Applications
- **Longitudinal Studies:** Track policy changes over time
- **Regional Analysis:** Focus on specific geographic areas
- **Drug-Specific Indices:** Separate measures for different substances
- **Micro-Level Analysis:** Subnational policy variation

### Research Opportunities
- **Policy Effectiveness Studies:** Correlation with outcome measures
- **Causal Analysis:** Natural experiments in policy changes
- **Network Analysis:** International cooperation patterns
- **Machine Learning:** Predictive modeling of policy outcomes

---

## 📞 Contact

**Primary Researcher:** [Your Name]  
**Email:** [your.email@institution.edu]  
**Institution:** [Your Institution]  
**Department:** [Your Department]

**Project Website:** [URL when available]  
**Repository:** [GitHub URL when available]

### For Questions About:
- **Methodology:** Contact primary researcher
- **Data Sources:** See data_sources.md or contact researcher
- **Technical Issues:** Check troubleshooting section first
- **Collaboration:** Open to academic partnerships

---

## 📝 Version History

| Version | Date | Changes | Status |
|---------|------|---------|---------|
| 1.0 | [Date] | Initial legal framework index | Complete |
| 2.0 | June 2025 | Added supply chain enforcement | Current |
| 2.1 | [Planned] | Additional countries | Planned |
| 3.0 | [Planned] | Temporal analysis | Future |

---

## ⚖️ License

This work is licensed under [Choose appropriate license - e.g., Creative Commons Attribution 4.0 International License]. 

You are free to:
- **Share:** Copy and redistribute the material
- **Adapt:** Remix, transform, and build upon the material

Under the following terms:
- **Attribution:** Provide appropriate credit and citation
- **Academic Use:** Primarily intended for research and educational purposes

---

## 🙏 Acknowledgments

- Thesis advisor: [Advisor Name]
- Data collection assistance: [Names if applicable]
- Expert consultations: [Expert names if applicable]
- Funding support: [Funding sources if applicable]

---

*Last updated: [Date]*  
*README version: 1.0*