class InsufficientFundsException extends Exception {
    public InsufficientFundsException(String message) {
        super(message);
    }
}

// The class below "BankAccount Class represents a bank account"
class BankAccount {
    private int accountNumber;
    private String accountHolderName;
    private double balance;

    public BankAccount(int accountNumber, String accountHolderName, double balance) {
        this.accountNumber = accountNumber;
        this.accountHolderName = accountHolderName;
        this.balance = balance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposited: " + amount + ", New Balance: " + balance);
        } else {
            System.out.println("Invalid deposit amount.");
        }
    }

    public void withdraw(double amount) throws InsufficientFundsException {
        if (amount > balance) {
            throw new InsufficientFundsException("Insufficient balance! Available balance: " + balance);
        }
        balance -= amount;
        System.out.println("Withdrawn: " + amount + ", Remaining Balance: " + balance);
    }

    public void displayAccountInfo() {
        System.out.println("Account Number: " + accountNumber + ", Holder: " + accountHolderName + ", Balance: " + balance);
    }
}

// Main class
public class BankingSystem {
    public static void main(String[] args) {
        BankAccount account1 = new BankAccount(101, "Satyam Singh", 500);
        BankAccount account2 = new BankAccount(102, "Nikunj Mathur", 1000);

        account1.displayAccountInfo();
        account2.displayAccountInfo();

        account1.deposit(200);
        account2.deposit(500);

        try {
            account1.withdraw(800);
        } catch (InsufficientFundsException e) {
            System.out.println("Exception: " + e.getMessage());
        }

        try {
            account2.withdraw(200);
        } catch (InsufficientFundsException e) {
            System.out.println("Exception: " + e.getMessage());
        }

        account1.displayAccountInfo();
        account2.displayAccountInfo();
    }
}
