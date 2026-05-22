import os
import shutil

def run_rename():
    # Revised mapping: target_filename -> slide number suffix
    # 100% sequential, duplicate-free mapping
    mapping = {
        "0.jpeg": "42.jpeg",       # 원래 표지
        "1.jpeg": "43.jpeg",       # 말씀 1
        "2.jpeg": "44.jpeg",       # 말씀 2
        "3.jpeg": "45.jpeg",       # 말씀 3
        "4.jpeg": "48.jpeg",       # 대속죄일 정의 시작
        "5.jpeg": "49.jpeg",       # 제비뽑기 / 번제
        "6.jpeg": "50.jpeg",       # 아사셀 염소 안수/전가
        "7.jpeg": "51.jpeg",       # 광야 길
        "8.jpeg": "52.jpeg",       # 염소 눈망울과 나의 죄
        "9.jpeg": "53.jpeg",       # 밧줄 풀며 선포
        "10.jpeg": "54.jpeg",      # 진짜 아사셀 예수님
        "11.jpeg": "55.jpeg",      # 성문 밖 골고다 길
        "12.jpeg": "56.jpeg",      # 자원하신 사랑 십자가
        "13.jpeg": "57.jpeg",      # 사탄에 맞선 약속 선포 (레위기 16:30)
        "ending.jpeg": "65.jpeg"   # 승리의 엔딩 이미지
    }
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Working directory: {current_dir}")
    
    # 1. Copy and rename according to mapping
    all_files = os.listdir(current_dir)
    success_count = 0
    
    for target, suffix in mapping.items():
        # Find a file in current_dir that ends with suffix
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
            
    # 2. Clean up original 슬라이드*.jpeg files (slides 42-65)
    print("\nCleaning up original slide files...")
    cleaned_count = 0
    for f in os.listdir(current_dir):
        # Match files that have numbers 42 to 65 in them and end with .jpeg
        if f.endswith(".jpeg") and not f[0].isdigit() and f != "ending.jpeg":
            # Extract number to verify it's between 42 and 65
            digits = "".join(filter(str.isdigit, f))
            if digits:
                num = int(digits)
                if 42 <= num <= 65:
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
