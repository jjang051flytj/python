#구글에서 만든 라이브러리 있음  비동기 동작
import googletrans
import asyncio
sing = """나는 행복합니다
나는 행복합니다
나는 행복합니다
정말 정말 행복합니다

기다리던 오늘 그날이 왔어요 즐거운 날이에요
움츠렸던 어깨 답답한 가슴을 활짝 펴봐요
가벼운 옷차림에 다정한 벗들과 즐거운 마음으로
들과 산을 뛰며 노래를 불러요 우리 모두 다 함께

나는 행복합니다
나는 행복합니다
나는 행복합니다
정말 정말 행복합니다

진달래꽃 피는 봄이 지나면 여름이 돌아와요
쏟아지는 태양 젊음이 있는 곳 우리들의 여름이죠
강에도 산에도 넓은 바다에 우리들의 꿈이 있어요
그곳으로 가요 노래를 불러요 우리 모두 다 함께

나는 행복합니다
나는 행복합니다
나는 행복합니다
정말 정말 행복합니다"""
async def main() :
    translator = googletrans.Translator()
    result01 = await translator.translate(sing, dest="vi")
    print(result01.text)
asyncio.run(main())