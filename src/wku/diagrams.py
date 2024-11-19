"""
Create slides showing the diagrams for APFRB and LERS studies.
"""

from src.oral_proposal.studies.lers import LERSDiagram
from src.oral_proposal.studies.apfrb import APFRBDiagram

if __name__ == "__main__":
    APFRBDiagram().render()
    # LERSDiagram().render()
