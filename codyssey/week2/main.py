import csv

# 파일 읽어서 리스트로 변환
def read_csv_to_list(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        print(f'파일을 찾을 수 없습니다: {filename}')
        return []
    except Exception as e:
        print(f'오류 발생: {e}')
        return []

# 인화성 지수(Flammability) 기준으로 내림차순 정렬
def sort_by_Flammability(data):
    return sorted(data, key=lambda x: float(x['Flammability']), reverse=True)

# 인화성 지수가 특정 값 이상인 항목 필터링
def filter_high_Flammability(data, threshold=0.7):
    return [item for item in data if float(item['Flammability']) >= threshold]

# CSV 파일로 저장
def write_list_to_csv(data, filename):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['Substance', 'Weight (g/cm³)', 'Specific Gravity', 'Strength', 'Flammability']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f'파일 저장 완료: {filename}')
    except Exception as e:
        print(f'파일 저장 중 오류 발생: {e}')



# 실행 부분
inventory_list = read_csv_to_list('Mars_Base_Inventory_List.csv')
print('\n---원본 데이터---')
for item in inventory_list:
    print(item)

sorted_inventory = sort_by_Flammability(inventory_list)

print('\n---인화성 내림차순 정렬 데이터---')
for item in sorted_inventory:
    print(item)

high_flammable_items = filter_high_Flammability(sorted_inventory)

print('\n---인화성 지수 0.7 이상인 물질---')
for item in high_flammable_items:
    print(item)

# 별도의 CSV 파일로 저장
write_list_to_csv(high_flammable_items, 'Mars_Base_Inventory_danger.csv')
