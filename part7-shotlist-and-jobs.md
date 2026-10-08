# Part 7 — I Heard You

**v1 (1:39):** https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/61c8de10-e570-44d9-873f-644d8621f599.mp4

Build: `python3 mb.py part7_edit_list.json && python3 score.py timeline.json part7_cues.json dlg.wav vid.mp4 out.mp4`
Shots: `tools/part7_shots.json` (generator `tools/part7_shots.py`). Every line checked word-for-word against the screenplay (whisper medium.en on the final mix).

## Caught and fixed before delivery
- Gym master: Ethan came out older with a receding hairline, Denise didn't match -> regenerated with their Part 6 close-ups as face references.
- Shot 10: Grace sat alone mid-bench (geometry broken vs shot 9) and over-acted shock -> regenerated as the reverse angle of shot 9.
- Shot 15: they KISSED (screenplay: she stops a breath away). Re-roll still touched because the start frame was too close -> new frame with a clear gap + "lips never touch".
- Shot 18: "when the board vote it's on" -> re-rolled ("votes on").
- Shot 4 voice change added "And"; shot 7 Kling added "Okay" -> `ss` trims.
- Shot 17 voice change dropped "'d" twice ("I better") -> Kling raw take.

## Frames (f7.json) / clips
```
{"8": "8094ad41-e3c8-4079-bdf5-1e559e1c112d", "18": "12b029c8-5d0e-45ce-aa4c-98a71b74a650", "19": "3a24fd2f-ba56-4054-9a1d-3616e0d01921", "1": "903d0f72-ae70-45e0-837e-231b9474e9f2", "20": "12b029c8-5d0e-45ce-aa4c-98a71b74a650", "9": "ffe53e08-ef45-4ff7-910b-c64385e51bd6", "15": "43eff90e-4365-4674-aed2-4ea6d1965b28", "2": "0b9ad47a-f629-4df8-9327-6f2a6477448f", "4": "965fe850-4764-45f7-b9f4-41f71bcf0fae", "11": "ffe53e08-ef45-4ff7-910b-c64385e51bd6", "13": "ffe53e08-ef45-4ff7-910b-c64385e51bd6", "17": "ffe53e08-ef45-4ff7-910b-c64385e51bd6", "6": "965fe850-4764-45f7-b9f4-41f71bcf0fae", "3": "0e9156a9-3137-4cd3-9edf-c1ec9b0bd000", "10": "c48e8f2f-0928-4451-90f9-59c1f55f94d1", "5": "0e9156a9-3137-4cd3-9edf-c1ec9b0bd000", "7": "0e9156a9-3137-4cd3-9edf-c1ec9b0bd000", "12": "c48e8f2f-0928-4451-90f9-59c1f55f94d1", "14": "c48e8f2f-0928-4451-90f9-59c1f55f94d1", "16": "c48e8f2f-0928-4451-90f9-59c1f55f94d1"}
--- raw
1 20261008_100321_4e2fca44-29e4-4dc7-9753-279ce7d11b50
2 20261008_100321_ac04eeea-39d6-4e1c-9c09-76aec366b2e5
3 20261008_100321_3012277e-8b9c-4edd-9271-3b1dfe99364b
4 20261008_100321_ddd2d6a0-2db7-41d9-91fc-0c9b6edde850
5 20261008_100321_513d6988-085f-44ec-8a41-069446bbcf2f
6 20261008_100321_67f19b2d-0ceb-4102-b2c3-d7fc559f1907
7 20261008_100321_834ab4e8-5d02-4c50-b7c2-d091e58dd55e
8 20261008_100321_934a50a8-3a35-4260-b7a7-f635cfc27d96
9 20261008_100321_c0bb8c44-3ff2-492e-b0b8-24058533f9f1
10 20261008_100321_3f875e84-899c-4baf-955a-c55773c61238
11 20261008_100325_9421a958-8017-47d9-bf90-b07e0824983b
12 20261008_100325_9c1949ce-ed24-4f84-a252-9cf0ec17e1a5
13 20261008_100325_406e9399-d448-46fa-bfb8-3f1c4f98965d
14 20261008_100326_852ad0b6-8b52-41eb-ad4b-b135cf374d2a
16 20261008_100325_8c836d16-4409-469c-b4be-a36d144b29ff
17 20261008_100325_cfadfd96-7ab0-48b2-b42a-08a4b720dafa
18 20261008_101106_9849d222-d995-4d50-bb99-57f65315e316
19 20261008_100325_84d158b3-d173-4c73-b1cf-50ee1093c30d
20 20261008_100325_b6558b01-daa0-427a-a98e-e2c0ea88c647
15 20261008_101645_181bd62a-ed16-4770-b981-07aa115e5bcc
--- voice-changed
3 hf_20261008_101245_5acaabcb-93f6-4c58-b743-bf628881a07a
4 hf_20261008_100944_01a4fc5b-f24a-4503-b3ed-31a5e875d51f
5 hf_20261008_100945_a5bcb029-a66b-4ea9-bbb0-a5ea418cb35a
6 hf_20261008_100944_808782a7-a22e-4b13-a4f2-f02e4bd857f1
9 hf_20261008_100944_b676573d-9e13-4d06-af69-7972cd5dbac4
10 hf_20261008_100945_e5f1b0d6-cb33-4567-89c0-aa827dcf41c2
11 hf_20261008_101546_26064f45-17ac-48d7-b8e0-63a9a6f03d33
12 hf_20261008_101243_e82cef0c-171b-4370-8e13-1ed9c0aaf826
13 hf_20261008_101243_29b754d0-9fbf-4e52-bffa-a632525db137
14 hf_20261008_101243_a04fc6db-602b-491b-9d1b-f7c50ee8c7cb
16 hf_20261008_101243_4cd0c72d-eb09-4609-9cc4-04282cd53c8d
18 hf_20261008_101648_afb2c83f-0dea-446d-a071-f6b313e3e1c3
19 hf_20261008_101547_6ed422b5-cddc-498f-8b5c-2efa24ef2a87
20 hf_20261008_101546_52ac5552-39eb-42c2-a2f8-1457751796f2
```
