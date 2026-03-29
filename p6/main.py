class TransactionError(Exception):
    pass

class InsufficientFundsError(TransactionError):
    pass

class InvalidAmountError(TransactionError):
    pass

class AuthError(Exception):
    pass


def log_operation(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG]: Виконується операція {func.__name__} з аргументами {args}.")
        return func(*args, **kwargs)
    return wrapper


def require_unlocked(func):
    def wrapper(self, *args, **kwargs):
        if not getattr(self, 'is_unlocked', False):
            raise AuthError("Операція відхилена: гаманець заблоковано.")
        return func(self, *args, **kwargs)
    return wrapper


class EWallet:
    def __init__(self, owner):
        self.owner = owner
        self._balance = 0
        self.is_unlocked = False

    def unlock(self):
        self.is_unlocked = True

    def lock(self):
        self.is_unlocked = False

    @log_operation
    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Сума операції повинна бути більшою за нуль.")
        self._balance += amount
        print(f"Баланс поповнено. Поточний баланс: {self._balance}")

    @log_operation
    @require_unlocked
    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Сума операції повинна бути більшою за нуль.")
        if amount > self._balance:
            raise InsufficientFundsError(f"Недостатньо коштів на рахунку. Поточний баланс: {self._balance}")
        self._balance -= amount
        print(f"Кошти знято. Поточний баланс: {self._balance}")

    def get_balance(self):
        return self._balance


if __name__ == "__main__":
    wallet = EWallet("User")

    try:
        wallet.withdraw(100)
    except AuthError as e:
        print(f"Помилка доступу: {e}")

    wallet.unlock()
    
    try:
        wallet.deposit(500)
    except TransactionError as e:
        print(f"Помилка транзакції: {e}")
        
    try:
        wallet.withdraw(600)
    except TransactionError as e:
        print(f"Помилка транзакції: {e}")
        
    try:
        wallet.deposit(-50)
    except TransactionError as e:
        print(f"Помилка транзакції: {e}")

