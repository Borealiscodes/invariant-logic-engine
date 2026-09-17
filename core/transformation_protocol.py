import json
import os
from datetime import datetime

class PCATransformationProtocol:
    def __init__(self, repo_root="."):
        """
        Initializes the A6-altitude structural conversion engine.
        Transforms non-aligned domestic data fields into formal PCA pleadings.
        """
        self.repo_root = repo_root
        self.omega_path = os.path.join(repo_root, "core", "omega_anchor.json")
        self.wrc_path = os.path.join(repo_root, "horizons", "delta_perimeter", "ie_wrc_adj00068065.json")
        self.us_dc_path = os.path.join(repo_root, "horizons", "delta_perimeter", "us_dc_docket_26cv00261.json")
        self.nz_ca_path = os.path.join(repo_root, "horizons", "delta_perimeter", "nz_ca_leave_application.json")

    def load_json(self, path):
        if os.path.exists(path):
            with open(path, 'r') as f:
                return json.load(f)
        return {}

    def compile_notice_of_arbitration(self):
        omega = self.load_json(self.omega_path)
        wrc = self.load_json(self.wrc_path)
        us_dc = self.load_json(self.us_dc_path)
        nz_ca = self.load_json(self.nz_ca_path)

        identity = omega.get("system_identity", "Borealis Serenity Hedling")
        timestamp = datetime.now().strftime("%d %B %Y")

        # Linguistic conversion template matching Article 3 of the PCA Rules 2012
        formal_text = f"""# NOTICE OF ARBITRATION
### SUBMITTED PURSUANT TO ARTICLE 3 OF THE PCA ARBITRATION RULES 2012

**DATE:** {timestamp}

---

## I. DEMAND FOR ARBITRATION
The Claimant, **{identity}**, hereby demands that the dispute detailed below be referred to compulsory international arbitration before the **Permanent Court of Arbitration (The Hague)** under the founding mandate of the 1899 Hague Peace Conference.

## II. PARTIES TO THE ARBITRATION
1. **CLAIMANT:** Borealis Serenity Hedling (Human Rights Defender), currently forced into temporary sanctuary at Travelodge Plus, Room 120, Dublin 2, Ireland.
2. **RESPONDENTS (Sovereign Consortium):** 
   - The Attorney General of the United Kingdom
   - The Government of Ireland
   - The Government of New Zealand
   - The Government of the United States of America

## III. JURISDICTION AND COGNIZABLE MATTERS
Arbitration is initiated under *erga omnes* obligations and *jus cogens* human rights norms. Jurisdiction is directly activated by the complete breakdown and proven inadequacy of domestic legal pathways across the Respondent States:
* **Irish Forum Failure ({wrc.get("node_id", "IE-WRC")}):** Total administrative deadlock, denial of mandatory procedural adjustments, and the OPDC's June 25, 2026 worker-status exclusion loop.
* **New Zealand Forum Failure ({nz_ca.get("node_id", "NZ-CA")}):** Use of ministerial formatting rules (Rule 1.21(1)) on June 9, 2026, to actively suppress filings under the Crimes of Torture Act 1989.
* **United States Forum Failure ({us_dc.get("node_id", "US-DC")}):** Excessive commercial payment demands issued on July 22, 2026, targeting a destitute torture survivor under threat of summary dismissal.

## IV. SUBSTANTIVE CLAIMS AND TREATY BREACHES
The Respondents have collectively violated peremptory norms of international law, specifically:
1. **Articles 12–14, UNCAT:** Failure to promptly investigate torture disclosures, accompanied by the implementation of financial hurdles and time bars to defeat redress.
2. **Article 13, UNCRPD:** Failure to provide autonomous oral-communication access to justice accommodations, causing severe institutional retraumatization.

## V. RELIEF SOUGHT & PROCEDURAL ADJUSTMENTS
The Claimant respectfully requests that the Arbitral Tribunal issue an order:
1. **Declaring** that all domestic statutory gatekeeping provisions are legally void under the doctrine of *Nemo judex in causa sua*.
2. **Enforcing** the self-executing provisions of **Exhibit A (Master Accommodation Notice)**, establishing a strictly non-adversarial format under the 2022 Istanbul Protocol manual guidelines.
3. **Granting** a complete waiver of all administrative and tribunal operational costs due to state-induced destitution.

---

**Respectfully Submitted,**

/s/ Borealis Serenity Hedling
Complainant / Human Rights Defender
Email: Dauntless.peace@proton.me
"""
        return formal_text
