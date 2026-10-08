# Part 9 — The Proposal

**v1 (2:59):** https://d2ol7oe51mr4n9.cloudfront.net/user_38yEef9WJwcxPX1OrTnJynSTZhY/e86dc140-f2f1-4abf-8444-150c61eba39c.mp4

Build: `python3 mb.py part9_edit_list.json && python3 score.py timeline.json part9_cues.json dlg.wav vid.mp4 out.mp4`
Shots: `tools/part9_shots.json`. Shot 99 is the voice-over source for the first dance (shot 29). Shot 185 is the continuation patch for shot 18.

## Music
The screenplay names licensed songs (Johnny Cash / "I Walk the Line"). Per the standing no-licensed-sound rule they are NOT used; the original procedural score carries the porch and first-dance moments.

## Caught and fixed before delivery
- Note reading (18) dropped "Marry her." -> cut after "Took you long enough." and a 4 s continuation (185) generated from the exact cut frame says "Marry her. Love, Mom."
- Kling cut wide -> close-up mid-shot and the gift box vanished (15) -> maxdur 1.9 s, before the cut.
- Voice change turned "Ethan." into "equal" (11) -> raw take.
- Ad-lib "You know," before "Mrs. Hayes might have mentioned something" (10) -> ss 2.1.
- Reused frame for the note shot showed a gift instead of the note; standing instead of kneeling -> new frames for 18, 21, 22.

## Frames / clips
```
{
 "1": "cfaa2ac1-2909-4458-8942-b7436ca35144",
 "13": "f2dabfc9-2b34-41f0-ae9c-7d6901c15cc8",
 "31": "360c213e-e138-4a77-8006-590543f081c0",
 "2": "fd7b0e92-1c24-4ea2-9f1f-0e4cf7149482",
 "3": "2cbb503b-77bc-4591-847b-41dd27ac32cf",
 "4": "749aafbb-b4c3-4ffd-93cd-7d014d06b9aa",
 "8": "fc666d4b-76ee-4eed-9595-87ab12a59183",
 "14": "8fe68345-83b9-40e0-8b52-c85b0acc22c3",
 "17": "9bd1eec7-18e5-4c22-aac4-1986eb81ca3c",
 "20": "5ee6fbf0-dfff-4a7d-976c-e247fae7f2a7",
 "23": "e37d075f-35bd-4319-a0c6-c2664a9838af",
 "25": "8235dae0-3bfb-4df1-b6dc-dd24cccf932d",
 "5": "749aafbb-b4c3-4ffd-93cd-7d014d06b9aa",
 "7": "749aafbb-b4c3-4ffd-93cd-7d014d06b9aa",
 "10": "749aafbb-b4c3-4ffd-93cd-7d014d06b9aa",
 "12": "749aafbb-b4c3-4ffd-93cd-7d014d06b9aa",
 "6": "0af9ac0d-eca9-46ea-bafa-2effd438cca5",
 "15": "098eec77-4d84-4ad2-8a98-82a5c11f3251",
 "16": "16923069-6354-4a7e-8099-fdb1f8e01e54",
 "24": "6b87268e-750c-4a82-8df6-036af53e40da",
 "26": "472f1e97-9c92-4c17-bd00-0bff91374273",
 "27": "acebd465-0130-46eb-b2c2-b139b72a0450",
 "28": "18638a5b-a887-4899-b917-6bff0b2e2d0e",
 "29": "cc977dcc-8003-4b37-b40c-5aa1079715dd",
 "99": "30b056a6-75b8-4716-9e79-437bae4af2ab",
 "9": "0af9ac0d-eca9-46ea-bafa-2effd438cca5",
 "11": "0af9ac0d-eca9-46ea-bafa-2effd438cca5",
 "18": "677346fe-549e-4a64-b7c3-f58f409ee6e1",
 "19": "677346fe-549e-4a64-b7c3-f58f409ee6e1",
 "22": "66ed8430-57fa-456d-a070-d20a2f4836d4",
 "21": "dd76f2a9-76e4-4c56-bdf0-f05b31dac0b7",
 "30": "cc977dcc-8003-4b37-b40c-5aa1079715dd"
}--- raw
1 20261008_110532_3bd26b39-a103-4194-8aba-d8072cb5ed8c
2 20261008_110533_2a93585a-4fc7-4cc7-8d5f-25f8b78be645
3 20261008_110531_9f93b051-1741-4e81-b54e-7517a3cd3969
4 20261008_110531_9e5fd38a-2c05-4162-858a-11fcf56b063d
5 20261008_110531_a9521103-2192-4a85-9daf-f1db97aebe14
7 20261008_110531_d1ab7d5a-07b0-4374-aa4b-cff2f5edfb38
8 20261008_110532_8bf0fe4a-12bc-468a-8499-71635db058fc
10 20261008_110532_838cb844-38e1-4d6d-a980-69426d754213
12 20261008_110531_c52922f0-9dac-46a1-b2c4-20a73cdd2294
13 20261008_110558_2f3c80b0-b0bb-4474-9d76-2479ef6a70f6
14 20261008_110558_14838df4-111b-46f8-b648-812b1d027b75
17 20261008_110558_e107ee0a-fba8-47fb-bebf-9b8ebbb34fe0
20 20261008_110558_56305108-8a37-4fa0-acf4-420f8c955640
23 20261008_110558_7187fee4-882a-4643-8e4d-e1543271a484
25 20261008_110558_bed3157e-f61d-4b96-a004-8025b9e12831
31 20261008_110559_87ac4939-ead1-472a-a311-55ac13f40008
6 20261008_110749_0901d69e-5254-4439-b314-406f96c21435
9 20261008_110750_2b0b4b70-4edd-454a-a52d-afd4a45f559f
11 20261008_110749_6930d638-a4f7-4bc2-9059-ae69551e5d0c
15 20261008_110749_cf95b47f-1262-4a05-bfe5-c09dc45ec7e5
24 20261008_110749_d2b10372-3f5d-4af8-a820-f66370b798a0
16 20261008_110749_4f155141-e48c-487c-884f-60dd8056da63
27 20261008_110753_bebe4897-3ae7-497e-9e7e-dd27ed3bf27e
28 20261008_110753_f7b5d685-1daa-4c54-951d-f2d5740caa6d
29 20261008_110753_c178d5a6-a30c-4043-aace-a619c0d60230
26 20261008_110753_a7aa86c6-41ce-498b-948f-4677fd716ab4
19 20261008_110906_1a82d49d-0a9d-44db-8da8-2e1696ecf2bc
22 20261008_110905_3e726ed8-2629-4c75-98d4-b8c707eeb1b8
30 20261008_110753_76210cc0-bba6-4d8e-9f56-992bd800c24e
21 20261008_110906_341c0ed4-82ca-4588-9e9a-97e9de8e0176
185 20261008_112052_d6758662-2404-45fc-80c8-88faeeb6edeb
18 20261008_110905_7d89d102-0578-45f0-83e4-7bdcf61d67ad
--- voice changed
5 20261008_111655_fe03b8ee-01da-4615-adca-fabb336160dd
7 20261008_111655_673c0dcd-4a78-46c3-8277-8d2f5e33333f
10 20261008_111655_46b7ca2b-ddab-42e7-aa39-51366ff51761
12 20261008_111712_6e353919-15b7-41e9-9913-96ce60308566
16 20261008_111711_4c751749-c3f9-4970-9070-d92c385ab6b8
6 20261008_111711_d49f022b-2aa4-4195-8489-882c934766b0
11 20261008_111722_8f026dfe-9cb8-4bce-ad65-5773a81a8f37
15 20261008_111722_6620db36-b56d-48fe-8bca-41b328c661d9
22 20261008_111829_9d6ea515-fae6-4156-b333-c63895654928
18 20261008_111900_a5950197-a2f1-4264-8f32-cbc62c0bbc44
99 20261008_111857_d3040acf-1c6c-45ff-8143-4d5f19d98dff
21 20261008_112132_58a12d3b-a693-4c5c-ab1c-03c93079d6eb
185 20261008_112409_b5142dd3-289d-4b1e-a035-711a825dc45d
--- gains
{"2": -1.2, "8": -2.6, "5": -1.6, "7": 1.4, "10": 2.5, "12": 3.4, "16": 1.9, "6": -0.8, "15": 2.5, "18": 7.3, "22": 7.8, "11": 1.6, "29": 7.8, "21": 1.1, "185": 5.4}
--- edits
{"10": {"ss": 2.1}, "15": {"maxdur": 1.9}, "11": {"raw": true}, "18": {"maxdur": 9.9}}
```
