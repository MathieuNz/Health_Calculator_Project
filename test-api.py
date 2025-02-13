import aiohttp
import asyncio
import json

async def test_bmi():
    async with aiohttp.ClientSession() as session:
       
        bmi_data = {
            "height": 1.75,
            "weight": 70
        }
        async with session.post('http://localhost:5000/bmi', json=bmi_data) as response:
            assert response.status == 200
            data = await response.json()
            assert data['operation'] == 'bmi'
            assert abs(data['result'] - 22.86) < 0.01
            print("BMI test passed ")

async def test_bmr():
    async with aiohttp.ClientSession() as session:
      
        bmr_data = {
            "height": 175,
            "weight": 70,
            "age": 25,
            "gender": "male"
        }
        async with session.post('http://localhost:5000/bmr', json=bmr_data) as response:
            assert response.status == 200
            data = await response.json()
            assert data['operation'] == 'bmr'
            assert abs(data['result'] - 1724.05) < 0.01
            print("BMR test passed ")

async def test_api_doc():
    async with aiohttp.ClientSession() as session:
       
        async with session.get('http://localhost:5000/api') as response:
            assert response.status == 200
            data = await response.json()
            assert data['name'] == "Health Calculator API"
            assert 'endpoints' in data
            print("API documentation test passed ")

async def main():
    print("Starting async API tests...")
    await asyncio.gather(
        test_bmi(),
        test_bmr(),
        test_api_doc()
    )
    print("All async tests completed successfully! ")

if __name__ == "__main__":
    asyncio.run(main())