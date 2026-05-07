def log_table_operation(source_table: str, target_table: str, operation_name: str):
    print("Operation:", operation_name)
    print("Source table:", source_table)
    print("Target table:", target_table)


def log_row_count(label: str, count_value: int):
    print(f"{label}: {count_value}")