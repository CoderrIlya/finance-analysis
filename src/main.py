import pandas as pd
import matplotlib.pyplot as plt

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df["amount"] = df["amount"].astype(float)
    df["month"] = df["date"].dt.to_period("M")
    return df

def basic_analysis(df: pd.DataFrame):
    print("\n=== ОБЩИЙ БАЛАНС ===")
    print(f"Баланс: {df['amount'].sum()}")

    expenses = df[df["amount"] < 0]

    print("\n=== РАСХОДЫ ПО КАТЕГОРИЯМ ===")
    grouped = expenses.groupby("category")["amount"].sum()
    print(grouped)

    print("\n=== САМАЯ БОЛЬШАЯ ТРАТА ===")
    print(expenses.loc[expenses["amount"].idxmin()])

    print("\n=== САМАЯ ДОРОГАЯ КАТЕГОРИЯ ===")
    print(grouped.idxmin())

def monthly_analysis(df: pd.DataFrame):
    print("\n=== ПО МЕСЯЦАМ ===")
    monthly = df.groupby("month")["amount"].sum()
    print(monthly)

def plot_expenses_by_category(df: pd.DataFrame):
    expenses = df[df["amount"] < 0]
    grouped = expenses.groupby("category")["amount"].sum()

    grouped.plot(kind="bar")
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    
    plt.savefig("reports/expenses_by_category.png")
    plt.close()

def plot_monthly(df: pd.DataFrame):
    monthly = df.groupby("month")["amount"].sum()

    monthly.plot()
    plt.title("Balance Over Time")
    plt.xlabel("Month")
    plt.ylabel("Amount")

    plt.savefig("reports/monthly_balance.png")
    plt.close()

def advanced_stats(df: pd.DataFrame):
    expenses = df[df["amount"] < 0]

    print("\n=== СРЕДНЯЯ ТРАТА ===")
    print(expenses["amount"].mean())

    print("\n=== КОЛИЧЕСТВО ТРАНЗАКЦИЙ ===")
    print(len(df))

def top_expenses(df: pd.DataFrame):
    expenses = df[df["amount"] < 0]

    print("\n=== ТОП-3 КАТЕГОРИИ РАСХОДОВ ===")
    grouped = expenses.groupby("category")["amount"].sum().sort_values()
    print(grouped.head(3))

def insights(df: pd.DataFrame):
    expenses = df[df["amount"] < 0]
    grouped = expenses.groupby("category")["amount"].sum()

    worst_category = grouped.idxmin()

    print("\n=== ИНСАЙТ ===")
    print(f"Больше всего денег уходит на: {worst_category}")

def save_report(df: pd.DataFrame):
    expenses = df[df["amount"] < 0]
    grouped = expenses.groupby("category")["amount"].sum()

    with open("reports/report.txt", "w", encoding="utf-8") as f:
        f.write("=== ФИНАНСОВЫЙ ОТЧЁТ ===\n\n")
        f.write(f"БАЛАНС: {df['amount'].sum()}\n\n")

        f.write("Расходы по категориям:\n")
        f.write(grouped.to_string())
        f.write("\n\n")

        f.write(f"Самая дорогая категория: {grouped.idxmin()}\n")

def main():
    df = load_data("data/transactions.csv")
    df = clean_data(df)

    print("Первые строки:")
    print(df.head())

    basic_analysis(df)
    monthly_analysis(df)
    plot_expenses_by_category(df)
    plot_monthly(df)
    advanced_stats(df)
    top_expenses(df)
    insights(df)
    save_report(df)

if __name__ == "__main__":
    main()