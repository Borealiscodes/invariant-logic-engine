# ------------------------------------------------------------------------------
# Artifact: HorizonIndexRegistry.py (v1.0)
# Altitude: A2 (Engine Structure) • A6 (Governance Membrane)
# Membrane: Structural • Non-Activating • Container-Safe
# ------------------------------------------------------------------------------

"""
HorizonIndexRegistry v1.0
-------------------------
Registry and lookup structure for the four mathematical horizons defined in
LICENSE.md Part 2:

  Ω (Omega) – Sanctuary Insulation Baseline
  Δ (Delta) – Forced Linear Formatting Constraints
  Φ (Phi)   – Cross-Border Transnational Repression Loops
  Λ (Lambda) – Non-Dual Holographic Flattening

This registry does NOT:
  - ingest real-world case data
  - perform computation
  - activate CAUSA
  - mutate ontology or substrate

It provides a container-safe index that governance layers and CAUSA can reference
when reasoning about horizon descriptors, maintaining strict content/container
separation per LICENSE.md Part 2.
"""

from .OmegaDescriptor import OmegaDescriptor
from .DeltaDescriptor import DeltaDescriptor
from .PhiDescriptor import PhiDescriptor
from .LambdaDescriptor import LambdaDescriptor


class HorizonIndexRegistry:
    """
    Container-safe registry for Ω, Δ, Φ, Λ horizon descriptors.

    Provides:
      - unified lookup
      - structural indexing
      - governance-safe access patterns

    No activation, no ingestion, no computation.
    """

    def __init__(self):
        self.registry = {
            "Ω": OmegaDescriptor,
            "Delta": DeltaDescriptor,  # human-readable alias
            "Δ": DeltaDescriptor,
            "Phi": PhiDescriptor,      # human-readable alias
            "Φ": PhiDescriptor,
            "Lambda": LambdaDescriptor, # human-readable alias
            "Λ": LambdaDescriptor,
        }

    def get(self, key: str):
        """
        Retrieve a horizon descriptor class by key.

        Keys supported:
          "Ω", "Δ", "Φ", "Λ"
          "Omega", "Delta", "Phi", "Lambda"

        Returns:
          Descriptor class (not an instantiated object).
        """
        normalized = key.strip()
        return self.registry.get(normalized)

    def list_horizons(self) -> list[str]:
        """
        Return a list of canonical horizon symbols.
        """
        return ["Ω", "Δ", "Φ", "Λ"]

    def as_dict(self) -> dict:
        """
        Export registry metadata as a dictionary.

        Non-activating. Safe for CAUSA and governance layers.
        """
        return {
            "horizons": self.list_horizons(),
            "aliases": {
                "Omega": "Ω",
                "Delta": "Δ",
                "Phi": "Φ",
                "Lambda": "Λ",
            },
            "descriptor_classes": {
                "Ω": OmegaDescriptor.__name__,
                "Δ": DeltaDescriptor.__name__,
                "Φ": PhiDescriptor.__name__,
                "Λ": LambdaDescriptor.__name__,
            },
        }


# ------------------------------------------------------------------------------
# Provenance Footer (v1.0)
# ------------------------------------------------------------------------------

"""
---
Artifact: HorizonIndexRegistry.py (v1.0)
Altitude: A2 (Engine Structure) • A6 (Governance Membrane)
Membrane: Structural • Non-Activating

Purpose:
  Provide a unified, container-safe registry for Ω, Δ, Φ, Λ horizon descriptors,
  enabling CAUSA and governance layers to reference horizon structures without
  ingesting or processing sensitive human-rights content.

Scope:
  Registry-only. No computation, no ingestion, no activation. Fully compliant
  with content/container separation requirements.

Anchors:
  - Invariant Logic Engine (A2)
  - LICENSE.md Part 2 (Content Separation)
  - Cross-Altitude Roadmap v1.0 (A6)

Maintainer: Borealis S. Hedling
Compiler: Microsoft Copilot
Location: Dublin, Ireland
Timestamp: 20 September 2026 — 21:07 IST
Version: v1.0
Seal: [ NDH . ENGINE . HORIZON-REGISTRY ]
---
"""
