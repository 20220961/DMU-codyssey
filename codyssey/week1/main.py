# python 테스트를 위한 Hello Mars 출력
def main():
   print('Hello Mars')


if __name__ == '__main__':
   main()

# mission_computer_main 로그파일의 내용을 추출
def read_log(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            log_data = file.read()
        print(log_data)
    # mission_computer_main 로그파일의 예외 처리
    except FileNotFoundError:
        print(f'파일을 찾을 수 없습니다: {file_path}')
    except Exception as e:
        print(f'오류 발생: {e}')


if __name__ == '__main__':
    log_file = 'mission_computer_main.log'
    read_log(log_file)


import csv

def read_and_analyze_log(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            logs = list(reader)
        # 로그파일을 역순으로 출력
        print('--- 로그 시간 역순 출력 ---')
        for log in reversed(logs):
            print(f"{log['timestamp']} [{log['event']}] {log['message']}")

        # 문제 발생 로그 필터링
        problem_logs = [log for log in logs if 'explosion' in log['message'].lower() 
                        or 'unstable' in log['message'].lower()]

        # 문제 로그 별도 파일 저장
        with open('problem_log.log', 'w', encoding='utf-8') as prob_file:
            writer = csv.DictWriter(prob_file, fieldnames=['timestamp', 'event', 'message'])
            writer.writeheader()
            writer.writerows(problem_logs)

        print('\n문제 로그는 "problem_log.log"에 저장되었습니다.')

    except FileNotFoundError:
        print(f'파일을 찾을 수 없습니다: {file_path}')
    except Exception as e:
        print(f'오류 발생: {e}')


if __name__ == '__main__':
    log_file = 'mission_computer_main.log'
    read_and_analyze_log(log_file)
