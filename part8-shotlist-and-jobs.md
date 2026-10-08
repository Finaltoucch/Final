# Part 8 — The Boardroom

**v1 (2:39):** https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/0eb7f965-1d3b-4781-a7fa-51253744d824.mp4

Build: `python3 mb.py part8_edit_list.json && python3 score.py timeline.json part8_cues.json dlg.wav vid.mp4 out.mp4`
Shots: `tools/part8_shots.json`. The "Play it" recording reuses the real Part 6 recorded lines (Vanessa shot 5, Bradley shot 6) as voice-over on shots 15-16.

## Caught and fixed before delivery
- Receptionist too far away for a speaking shot (2) -> closer frame.
- Boardroom table EMPTY when the doors open (7) -> board seated.
- Blurred listener had grey hair, not Ethan (8, 26) -> regenerated with Ethan's very dark hair.
- Vanessa missing from the table (10); Bradley still at the head after giving up his chair (15, twice) -> fixed seating; Bradley sits beside Vanessa from shot 12 on.
- "Harold" already seated at the far end while standing at the door (9) -> removed.
- Board chair missing from the table in the recording shot although he seconds later (15) -> added back.
- Bradley and Vanessa voting for their own removal (22) -> hands down; Latino board member votes in the animation.
- Vanessa's hands free after being cuffed (28) -> cuffed behind her back.
- Ethan's cane vanished mid-shot (5, three takes) -> shot cut at 4.3 s, rest of his line plays over a new Grace reaction cutaway (builder `vo_ss`).
- Ethan never sat in the head chair (10) -> trimmed to the step-aside.
- "Second" for "Seconded" (20); "Caldwell's acting CEO" (19); "Oh, I understand" (11) -> re-rolls / trim.
- Voice change garbled "All in favor" -> "All in shaver" twice (21) -> raw take.
- Kling added "Thank you" over the applause (30) -> clip audio muted, score carries it.

## Frames / clips
```
{"1": "7ae396b9-e8b1-4271-8e1d-0825cf265a76", "6": "68fc6091-813f-48e3-b604-94767301b98b", "3": "1d069125-45b2-4ccf-b34a-aa5f2273516f", "5": "615a3363-5492-46ce-850b-44d274cb70ad", "14": "112b14bf-feaa-48f1-b1b7-ba656635c028", "16": "9e271545-1cc6-4eb4-b7bf-d7bdd734c366", "17": "5c691aa4-722b-4015-863d-18aeff701e9f", "20": "ef2b8ce8-aed8-4864-bf4a-8006d2032aa3", "2": "3877dd26-15ea-452e-b47f-0cb07242f4f7", "4": "248680ec-c8f6-4877-8bb5-6f4be0d40c7a", "7": "b166138a-2a2f-4d4d-b0f4-04d74175c130", "8": "751fcbb9-5e53-4934-92c0-f6418dca8a2a", "10": "bb98c5c7-172b-437b-b537-f5b867d84f09", "25": "318a137b-3740-43b6-9b65-b7546c098d5f", "30": "6ed19771-a90f-4cf4-a521-1c51e47cb73b", "32": "1fb10a17-fe1c-48e2-bbfb-9d0cfca7186b", "12": "1012b935-066b-418f-9db2-7ba737fc2a50", "18": "b5c50899-10cf-489b-9cba-9c8e04af336c", "23": "d81a6d94-9279-47ff-b72d-979ec03e8bd9", "26": "6ce35c5e-eb5d-452b-9cd3-27530a9604fd", "28": "537b36a0-de47-4ca4-9444-8d5bd57c0265", "29": "620fa36b-52c5-419a-ba93-50b4d9431fc0", "31": "d6d9d337-1059-4429-86f0-bae1ef261aae", "9": "cccd6382-ae99-4d58-9603-b2213011215b", "15": "63848d16-4cab-4513-b1e2-5412ed45b5d3", "11": "62f761f1-c1a4-422f-9550-bf59d87965a4", "24": "eb1a3faa-2aef-4a20-9d39-279a8cc16cf2", "13": "62f761f1-c1a4-422f-9550-bf59d87965a4", "19": "62f761f1-c1a4-422f-9550-bf59d87965a4", "21": "62f761f1-c1a4-422f-9550-bf59d87965a4"}
--- raw
1 20261008_103119_8cf1fe8b-9866-457a-8e81-63550d9238d7
2 20261008_103119_c896abd0-31ea-4755-b692-e918c9cc13b5
3 20261008_103119_12f70ee6-cfd2-4449-8eee-63f50089c597
4 20261008_103119_c456165a-a2e5-4c8b-a26a-eeea2e04ccc4
5 20261008_104310_c977927f-e8df-400e-91ab-65c87ae2f88d
6 20261008_103120_e7826c99-cca8-4fe9-b0df-6d8df806f652
7 20261008_103119_b8deaf09-ac17-4afb-a2a7-c4ac74830843
8 20261008_103119_99268ddb-b3d3-4b3b-9454-adccbaa582bd
9 20261008_103640_c1203244-cf75-4653-9d46-e35f1b2cdce9
10 20261008_103304_0e602553-23a9-4ccb-ad2a-091042b6e0b3
11 20261008_103640_b0f3d197-8cc3-4128-acde-5b38bce4cd9d
12 20261008_103304_b3fe94a9-3fa7-45d9-a0b2-08530c7cac06
13 20261008_103640_ef4ff0a0-b280-49eb-b6a2-27dec07b6476
14 20261008_103150_8bbcc767-a15e-4ad5-a7f3-088b4f582d7e
15 20261008_103640_aebd352e-db73-48a0-afbd-71c435b3746b
16 20261008_103148_6d1e6b03-88b2-4450-8028-80552649f4d5
17 20261008_103148_c2331e60-a5ea-49ef-831a-608ae3b0d35f
18 20261008_103304_5ed46a60-6a24-42c5-9a40-474e8d5ecf95
19 20261008_104309_f079e392-c8d9-4726-97be-8880a0c06233
20 20261008_103817_eb4eb6d9-2d64-4c0d-a4d8-158a9288c002
21 20261008_103640_9c14fddb-a812-4693-a4c8-9a5385e4f7b7
22 20261008_103742_d35c39df-6808-4d15-92fa-9d48f34a88b2
23 20261008_103304_5bdcb094-3a04-41cf-88aa-4833b2a76949
24 20261008_103640_bddd350b-2244-4194-b149-ba9ee87d6206
25 20261008_103148_62925938-5863-4274-8d7f-aab73d282f06
26 20261008_103304_9dfcb536-7d1c-485e-b109-45537a809700
27 20261008_103932_55bae5a1-d178-4b35-9f10-b9e8a4245222
28 20261008_103304_be858ef8-f185-4cb4-9395-a4bb32eec4ca
29 20261008_103304_5e18ce86-1321-44ac-a91a-b4caa6ff0bb5
30 20261008_103148_251b7165-cc86-4f02-bc60-8b7acdf648dc
31 20261008_103304_1fdf5d17-6b1e-4bc2-8298-24b1070aee18
32 20261008_103148_b05d3198-96a1-4ab6-aaff-572c22ad5acc
--- voice-changed
4 hf_20261008_104334_63dd66f9-cc81-46dc-ae17-c07f90f340fa
5 hf_20261008_104830_697f5687-003c-430a-a677-8a087a453c82
8 hf_20261008_104335_0193583f-a3c5-4284-916a-57292d684ff2
9 hf_20261008_104335_38f21cf0-ab3a-4c7e-9ea7-2ae576eda6b4
11 hf_20261008_104335_fa135d22-0f8e-424a-b085-b0e8ff1d9abc
12 hf_20261008_104339_e31e7a11-f8f5-4370-9784-1b194c750f22
13 hf_20261008_104353_53404756-ed67-4fb6-ba41-20a409e63a0e
17 hf_20261008_104335_bb948549-65c7-44d6-b4cf-91c62f838a95
19 hf_20261008_104830_b2ca7e47-0038-48a2-bed8-c7a3cc283462
26 hf_20261008_104353_3f9b9e36-c5c1-4281-80e8-a970d2b53b4b
27 hf_20261008_104639_e4641735-96bf-45eb-84ba-7870f1e319d0
31 hf_20261008_104353_30e4eeb9-3dc5-4cc5-b948-2c722123606a
32 hf_20261008_104353_4e0675c3-24b5-4c24-a5e8-479bd631dfb7
--- reaction 55: 20261008_104818_61d4b894-5aa2-412b-8293-8d04f26f6a79
```
