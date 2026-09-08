import uuid
from abc import ABC, abstractmethod
from typing import Dict, Any


class PaymentProvider(ABC):

    @abstractmethod
    def process_payment(self, amount: float, currency: str = "USD", payment_method: str = "CARD") -> Dict[str, Any]:
        """Process payment attempt with gateway."""
        pass

    @abstractmethod
    def refund_payment(self, transaction_id: str, amount: float) -> Dict[str, Any]:
        """Process refund with gateway."""
        pass


class MockPaymentProvider(PaymentProvider):

    def process_payment(self, amount: float, currency: str = "USD", payment_method: str = "CARD") -> Dict[str, Any]:
        """Simulate successful payment processing without external API credentials."""
        tx_id = f"tx_mock_{uuid.uuid4().hex[:12]}"
        return {
            "success": True,
            "transaction_id": tx_id,
            "status": "PAID",
            "amount": amount,
            "currency": currency,
            "message": "Mock payment processed successfully."
        }

    def refund_payment(self, transaction_id: str, amount: float) -> Dict[str, Any]:
        """Simulate refund processing."""
        return {
            "success": True,
            "transaction_id": f"ref_{transaction_id}",
            "status": "REFUNDED",
            "amount": amount,
            "message": "Mock payment refunded successfully."
        }


def get_payment_provider() -> PaymentProvider:
    """Factory returning configured payment provider (MockPaymentProvider by default)."""
    return MockPaymentProvider()
