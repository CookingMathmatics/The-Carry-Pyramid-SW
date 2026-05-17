"""
Physical Ghost - Basic Active Deception Trap Example
====================================================
본 예제는 피지컬 고스트 API를 활용하여 지정된 포트에
다차원 위상 감옥(Tar-Pit)을 전개하는 기본 뼈대입니다.

[주의] 본 스크립트를 실행하기 전, 와디즈 리워드로 제공받은
정식 라이선스 키를 반드시 입력해야 엔진이 가동됩니다.
"""

import sys
import time
from physical_ghost import GhostEngine, TopologicalTrap

# 1. 와디즈 후원자 라이선스 키 입력 (이메일 발송분)
WADIZ_LICENSE_KEY = "YOUR_WADIZ_LICENSE_KEY_HERE"

# 2. 방어선을 구축할 타겟 포트 설정 (예: 22번 SSH 포트를 미끼로 사용)
TARGET_PORT = 22

def main():
    print("🚀 Physical Ghost: Initiating Active Deception Protocol...")
    
    # 코어 엔진 인증 및 초기화
    engine = GhostEngine(license_key=WADIZ_LICENSE_KEY)
    
    if not engine.authenticate():
        print("[!] License Verification Failed. Please check your Wadiz API Key.")
        sys.exit(1)
        
    print("[+] License Verified. Loading p-adic Carry Dynamics...")
    
    # 위상 감옥(Tar-Pit) 생성 및 포트 바인딩
    trap = TopologicalTrap(engine, port=TARGET_PORT)
    
    try:
        # 방어선 가동 (비인가 접근 발생 시 무한 루프로 격리)
        trap.deploy()
        print(f"[*] Topological Trap is now ACTIVE on port {TARGET_PORT}.")
        print("[*] Waiting for unauthorized scanners... (Press Ctrl+C to stop)")
        
        # 메인 루프 유지
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n[-] Admin requested shutdown. Safely closing the topological maze.")
        trap.shutdown()
        sys.exit(0)

if __name__ == "__main__":
    main()
