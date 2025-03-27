import csv

# CSV 파일 내용을 그대로 출력하는 함수
def print_csv_contents(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print('\n--- CSV 파일 원본 내용 ---')
            print(content)
    except FileNotFoundError:
        print(f'파일을 찾을 수 없습니다: {filename}')
    except Exception as e:
        print(f'오류 발생: {e}')

# CSV 파일 읽어서 리스트로 변환하는 함수
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

# 인화성 지수로 내림차순 정렬
def sort_by_Flammability(data):
    return sorted(data, key=lambda x: float(x['Flammability']), reverse=True)

# 인화성 지수 0.7 이상 필터링
def filter_high_Flammability(data, threshold=0.7):
    return [item for item in data if float(item['Flammability']) >= threshold]

# 리스트 데이터를 CSV 파일로 저장하는 함수
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
csv_filename = 'Mars_Base_Inventory_List.csv'

# 1단계: CSV 파일 원본 내용을 출력
print_csv_contents(csv_filename)

# 2단계: CSV 파일 내용을 읽어 리스트 객체로 변환
inventory_list = read_csv_to_list(csv_filename)

print('\n---리스트 객체로 변환된 데이터---')
for item in inventory_list:
    print(item)

# 3단계: 인화성 지수로 정렬
sorted_inventory = sort_by_Flammability(inventory_list)
print('\n---인화성 지수 내림차순으로 정렬된 데이터---')
for item in sorted_inventory:
    print(item)

# 4단계: 인화성 지수가 0.7 이상인 물질만 필터링
high_flammable_items = filter_high_Flammability(sorted_inventory)
print('\n---인화성 지수 0.7 이상인 물질---')
for item in high_flammable_items:
    print(item)

# 5단계: 필터링된 데이터를 별도의 CSV로 저장
write_list_to_csv(high_flammable_items, 'Mars_Base_Inventory_danger.csv')
