### MCP란?
- 기본적으로 AI와 외부 시스템간의 다리역할하는 연결 표준방식

1. 아키텍처 구성요소
    1) MCP Server : 데이터/도구/프롬프트를 제공하는 서버
    2) MCP Client : 서버와 통신하는 클라이언트 (중계 역할 : Gateway)
    3) MCP Host : 실제 애플리케이션 (직접 만든 langgraph agent)

2. 주요 기능
    - Resource : 파일, 데이터베이스
    - Tools : 도구
    - Prompts : 해보니까 성능 잘 뽑아내는 프롬프트가 있을 경우 제공 :
        (예 : Few shot 제공)