from beartype import beartype


class BankAccount:
    # 类属性：被所有实例共享
    bank_name = "Python Central Bank"

    def __init__(self, owner_name: str, initial_balance: float = 0.0):
        """
        初始化方法（构造函数）
        :param owner_name: 户主姓名
        :param initial_balance: 初始余额，默认为0.0
        """
        # 实例属性：每个实例独有
        self.owner_name = owner_name
        self.balance = initial_balance

        # 私有属性：以双下划线开头，外部无法直接访问
        self.__is_frozen = False

    def deposit(self, amount: float) -> None:
        """实例方法：存款"""
        if amount <= 0:
            print("存款金额必须大于0")
            return

        self.balance += amount
        print(f"成功存入 {amount:.2f} 元，当前余额为 {self.balance:.2f} 元")

    @beartype     # 使用 beartype 进行类型检查
    def withdraw(self, amount: float) -> bool:
        """实例方法：取款，返回是否成功"""
        if self.__is_frozen:
            print("账户已冻结，无法取款！")
            return False

        if amount > self.balance:
            print("余额不足！")
            return False

        self.balance -= amount
        print(f"成功取出 {amount:.2f} 元，当前余额为 {self.balance:.2f} 元")
        return True

    @classmethod
    def get_bank_name(cls) -> str:
        """类方法：访问类属性"""
        return cls.bank_name

    @staticmethod
    def is_valid_amount(amount: float) -> bool:
        """静态方法：与类和实例状态无关的工具函数"""
        return isinstance(amount, (int, float)) and amount > 0


# ================= 演示如何使用这个类 =================

# 1. 实例化对象 (创建账户)
account_alice = BankAccount("Alice", 1000.0)
account_bob = BankAccount("Bob")

# 2. 调用实例方法
account_alice.deposit(500.5)     # 存款
account_alice.withdraw(200.0)    # 取款
account_alice.withdraw(2000.0)   # 余额不足测试

# 3. 访问实例属性和类属性
print(f"\nAlice 的户主姓名: {account_alice.owner_name}")
print(f"Alice 的当前余额: {account_alice.balance}")
print(f"开户行 (通过实例访问): {account_alice.bank_name}")
print(f"开户行 (通过类方法访问): {BankAccount.get_bank_name()}")

# 4. 使用静态方法
print(f"\n100 是有效金额吗? {BankAccount.is_valid_amount(100)}")
print(f"-50 是有效金额吗? {BankAccount.is_valid_amount(-50)}")

# 5. 私有属性演示 (尝试访问会报错)
try:
    print(account_alice.__is_frozen)
except AttributeError as e:
    print(f"\n尝试直接访问私有属性报错: {e}")

# 正确的访问方式 (Python的名字改写机制 Name Mangling)
print(f"通过名字改写访问私有属性: {account_alice._BankAccount__is_frozen}")
