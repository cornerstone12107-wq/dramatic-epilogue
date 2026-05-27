import os
import shutil

def run_rename():
    # Mapping for "한 걸음 더" (레위기 19장)
    mapping = {
        "0.jpeg": "42.jpeg",       # 한 걸음 더 표지
        "1.jpeg": "53.jpeg",       # 레위기 1장에서 막히는 구간 (강 예화)
        "2.jpeg": "55.jpeg",       # <나는 자연인이다> 오해
        "3.jpeg": "58.jpeg",       # 진짜 거룩의 현장 (농장, 일터)
        "4.jpeg": "60.jpeg",       # 레위기 19:9 밭 모퉁이
        "5.jpeg": "62.jpeg",       # 일상의 모퉁이 (노트/식사 써클)
        "6.jpeg": "64.jpeg",       # 사소한 배려 (충전기/체육복)
        "7.jpeg": "65.jpeg",       # 히브리어 네 이웃을 사랑하라
        "8.jpeg": "69.jpeg",       # 부러진 다리 (엔진 없는 지도)
        "9.jpeg": "71.jpeg",       # 성령강림 (3000명 살림)
        "10.jpeg": "73.jpeg",      # 스르르 풀리는 움켜쥔 주먹
        "11.jpeg": "74.jpeg",      # 예수님의 생명 전부 비우신 사랑
        "12.jpeg": "75.jpeg",      # 내일의 교실로의 모험
        "13.jpeg": "48.jpeg",      # 말씀 제목 (한 걸음 더)
        "ending.jpeg": "42.jpeg"   # 승리의 엔딩 이미지 (표지 활용)
    }
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Working directory: {current_dir}")
    
    # 1. Copy and rename according to mapping
    all_files = os.listdir(current_dir)
    success_count = 0
    
    for target, suffix in mapping.items():
        # Find a file in current_dir that ends with suffix (handling different NFC/NFD unicode formats in mac)
        source_file = None
        for f in all_files:
            if f.endswith(suffix):
                source_file = f
                break
                
        if source_file:
            src_path = os.path.join(current_dir, source_file)
            dst_path = os.path.join(current_dir, target)
            try:
                shutil.copy2(src_path, dst_path)
                print(f"✓ Copied: {source_file} -> {target}")
                success_count += 1
            except Exception as e:
                print(f"✗ Error copying {source_file} to {target}: {e}")
        else:
            print(f"⚠ Warning: Slide ending with '{suffix}' not found in images folder.")
            
    # 2. Clean up original 슬라이드*.jpeg files (slides 42-75)
    print("\nCleaning up original slide files...")
    cleaned_count = 0
    for f in os.listdir(current_dir):
        # Match files that have numbers 42 to 75 in them and end with .jpeg
        if f.endswith(".jpeg") and not f[0].isdigit() and f != "ending.jpeg":
            # Extract number to verify it's between 42 and 75
            digits = "".join(filter(str.isdigit, f))
            if digits:
                num = int(digits)
                if 42 <= num <= 75:
                    file_path = os.path.join(current_dir, f)
                    try:
                        os.remove(file_path)
                        print(f"✓ Cleaned: {f}")
                        cleaned_count += 1
                    except Exception as e:
                        print(f"✗ Error removing {f}: {e}")
                        
    print(f"\n==================================================")
    print(f"🎉 Complete! Mapped {success_count} files, Cleaned {cleaned_count} original slides.")
    print(f"==================================================")

if __name__ == "__main__":
    run_rename()
