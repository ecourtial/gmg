from src.controller.abstract_controller import AbstractController
from src.repository.transaction_repository import TransactionRepository
from src.service.transaction_service import TransactionService

class TransactionController(AbstractController):
    repository = TransactionRepository
    service = TransactionService
