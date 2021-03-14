-- 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

-- 코딩테스트 연습 > SQL > IS NULL
-- 이름이 없는 동물의 아이디
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME IS NULL;

-- 이름이 있는 동물의 아이디
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL;

-- NULL 처리하기
SELECT ANIMAL_TYPE,
    CASE
        WHEN NAME IS NULL THEN 'No name'
        ELSE NAME 
        END NAME,
    SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

-- 코딩테스트 연습 > SQL > STRING, DATE
-- 루시와 엘라 찾기
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('lUCY', 'ELLA', 'Pickle', 'Rogan', 'Sabrina', 'Mitty');

-- 이름에 el이 들어가는 동물 찾기
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%el%' AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME;

-- 중성화 여부 파악하기
SELECT ANIMAL_ID, NAME,
    CASE
        WHEN SEX_UPON_INTAKE LIKE '%Neutered%' THEN 'O'
        WHEN SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
        ELSE 'X'
        END 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

-- DATETIME에서 DATE로 형 변환
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d')
FROM ANIMAL_INS
ORDER BY ANIMAL_ID; 