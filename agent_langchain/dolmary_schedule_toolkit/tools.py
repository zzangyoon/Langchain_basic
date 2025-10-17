from typing import List, Type
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field

# 스케줄 등록하는 리스트
# 1. 스케줄 등록 도구
# 2. 스케줄 확인 도구
# 3. 스케줄 삭제 도구
dol_schedule : List[str] = []

#############################
# 1. 스케줄 등록 도구
#############################
# 1-1. 스케줄 등록 schema 설정
class AddToDoInput(BaseModel):
    item : str = Field(description="오늘 할 돌마리 스케줄 항목")

# 1-2. 스케줄 등록 도구 설정
class AddToDoTool(BaseTool):
    name : str = "add_toDo"
    description : str = "돌마리 스케줄에 새 항목을 추가합니다"
    args_schema : Type[BaseModel] = AddToDoInput

    def _run(self, item: str) -> str:
        dol_schedule.append(item)
        return f"{item}이 돌마리 할일 스케줄에 등록되었습니다"


#############################
# 2. 스케줄 확인 도구
#############################
# 2-1. 스케줄 확인 schema 설정 -> 필요 없을듯

# 2-2. 스케줄 확인 도구 설정
class ViewToDoTool(BaseTool):
    name : str = "view_toDos"
    description : str = "현재 돌마리 스케줄 전체 목록을 보여줍니다"

    def _run(self):
        if not dol_schedule:
            return "할일이 없어요"
        all_schedule = "\n".join(dol_schedule)
        return f"할일 목록은 : {all_schedule}\n입니다"


#############################
# 3. 스케줄 삭제 도구
#############################
# 3-1. 스케줄 삭제 schema 설정
class DeleteToDoList(BaseModel):
    item : str = Field(description = "삭제할 돌마리 스케줄 항목")

# 3-2. 스케줄 삭제 도구 설정
class DeleteTodoTool(BaseTool):
    name : str = "delete_toDo"
    description : str = "돌마리 스케줄 중 항목을 삭제합니다"
    args_schema : Type[BaseModel] = DeleteToDoList

    def _run(self, item: str) -> str:
        if item in dol_schedule:
            dol_schedule.remove(item)
            return f"{item}이 돌마리 스케줄에서 삭제되었습니다"
        else:
            return f"'{item}' 항목은 현재 돌마리 스케줄에 없습니다"
        

#############################
# 4. 스케줄 완료 도구
#############################
# 4-1. 스케줄 완료 schema 설정
class CompleteToDoInput(BaseModel):
    item : str = Field(description = "완료 처리할 돌마리 스케줄 항목")

# 4-2. 스케줄 완료 도구 설정
class CompleteTodoTool(BaseTool):
    name : str = "complete_toDo"
    description : str = "돌마리 스케줄 항목을 완료된 상태로 표시합니다"
    args_schema : Type[BaseModel] = CompleteToDoInput

    def _run(self, item: str) -> str:
        for i, todo_item in enumerate(dol_schedule):
            if todo_item == item:
                if "[완료]" in todo_item:
                    return f"'{item}' 항목은 이미 완료 처리되어 있습니다."
                dol_schedule[i] = todo_item + " [완료]"
                return f"'{item}' 항목을 완료 처리했습니다."
        return f"'{item}' 항목을 스케줄에서 찾을 수 없습니다."