import re
from typing import List
from sqlalchemy.orm import Session
from app.schemas.ai_recommendations import (
    DiagnosticWizardRequest, DiagnosticRecommendation,
    ProblemKeywordPricingRequest, ProblemKeywordPricingResponse,
    HealthRiskAssessmentResponse
)


class AIRecommendationService:

    @staticmethod
    def run_diagnostic_wizard(db: Session, req: DiagnosticWizardRequest) -> DiagnosticRecommendation:
        app_type = req.appliance_type.lower()
        symptoms_str = " ".join(req.symptoms).lower()

        root_cause = "General Component Wear & Tear"
        cat = "General Repair"
        cost_range = "$50.00 - $120.00"
        urgency = "MEDIUM"
        confidence = 88.5
        action = "Book a certified technician for diagnostic check."

        if "cooling" in symptoms_str or "warm air" in symptoms_str:
            root_cause = "Refrigerant Gas Leakage / Compressor Failure"
            cat = "AC Repair"
            cost_range = "$80.00 - $250.00"
            urgency = "HIGH"
            confidence = 94.2
            action = "Recommend Gas Refill & Compressor Pressure Audit."
        elif "water" in symptoms_str or "leak" in symptoms_str:
            root_cause = "Drain Line Clog / Pump Seal Failure"
            cat = "Plumbing & Appliance Maintenance"
            cost_range = "$45.00 - $95.00"
            urgency = "MEDIUM"
            confidence = 91.0
            action = "Clear drain tube blockage and replace filter seal."
        elif "noise" in symptoms_str or "grinding" in symptoms_str:
            root_cause = "Blower Motor Bearing Wear / Loose Fan Blade"
            cat = "Electrical & Motor Repair"
            cost_range = "$60.00 - $140.00"
            urgency = "MEDIUM"
            confidence = 86.8
            action = "Inspect motor assembly and lubricate fan bearings."

        return DiagnosticRecommendation(
            diagnosed_root_cause=root_cause,
            suggested_service_category=cat,
            estimated_cost_range=cost_range,
            urgency_level=urgency,
            confidence_score_percent=confidence,
            recommended_action=action
        )

    @staticmethod
    def estimate_problem_pricing(req: ProblemKeywordPricingRequest) -> ProblemKeywordPricingResponse:
        desc = req.problem_description.lower()
        keywords = []

        labor = 49.0
        parts = 0.0

        if "ac" in desc or "air conditioner" in desc:
            keywords.append("AC")
            labor = 79.0
        if "refrigerator" in desc or "fridge" in desc:
            keywords.append("Refrigerator")
            labor = 69.0
        if "leak" in desc or "water" in desc:
            keywords.append("Leakage")
            parts += 25.0
        if "gas" in desc or "cooling" in desc:
            keywords.append("Gas Refill")
            parts += 60.0
        if "noise" in desc or "grinding" in desc:
            keywords.append("Motor Issue")
            parts += 45.0

        total = labor + parts

        return ProblemKeywordPricingResponse(
            detected_keywords=keywords or ["General Maintenance"],
            estimated_labor_cost=labor,
            estimated_parts_cost=parts,
            total_estimated_price=total,
            suggested_service_ids=[1, 2]
        )

    @staticmethod
    def assess_appliance_health(brand: str, appliance_type: str, age_years: int) -> HealthRiskAssessmentResponse:
        risk_pct = min(95.0, max(5.0, age_years * 12.5))

        status_str = "EXCELLENT"
        rec = "Annual preventative inspection recommended."
        if risk_pct > 70.0:
            status_str = "HIGH_RISK_CRITICAL"
            rec = "High failure risk due to age. Consider AMC Plan protection or component overhaul."
        elif risk_pct > 35.0:
            status_str = "FAIR"
            rec = "Moderate risk. Clean filters and inspect coils every 6 months."

        return HealthRiskAssessmentResponse(
            appliance_brand=brand,
            appliance_type=appliance_type,
            age_years=age_years,
            failure_risk_percentage=risk_pct,
            health_status=status_str,
            recommended_maintenance=rec
        )

AiRecommendationsService = AIRecommendationService
