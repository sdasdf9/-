total_capsules = int(input("Введите общее количество произведенных капсул: "))
package_capacity = int(input("Введите количество капсул в одной упаковке: "))
full_packages = total_capsules // package_capacity
remaining_capsules = total_capsules % package_capacity
print("\n--- Отчет фасованного цеха ---")
print(f"Полных упаковок: {full_packages}")
print(f"Остаток капсул: {remaining_capsules}")