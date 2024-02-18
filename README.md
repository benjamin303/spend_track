# spend_track
Expense tracker using Django

ToDO:
Plans (plans for expenses like buying motorcycle) (calculate balance after that ...)


Expense Categories and Subcategories

Housing
    Rent/Mortgage
    Property Taxes
    Home Insurance
    Maintenance & Repairs
    Utilities (consider breaking this into subcategories as below)

Utilities
    Electricity
    Gas
    Water
    Sewage
    Trash Removal
    Internet
    Cable/Satellite TV

Food
    Groceries
    Dining Out
    Fast Food
    Coffee Shops
    Food Delivery

Transportation
    Public Transit
    Fuel
    Car Payments
    Auto Insurance
    Maintenance & Repairs
    Parking Fees
    Taxis/Ride-Sharing

Healthcare
    Health Insurance
    Doctor/Dentist Visits
    Prescriptions
    Over-the-Counter Medications
    Medical Supplies

Insurance (Non-Health)
    Life Insurance
    Disability Insurance
    Personal Liability Insurance
    Travel Insurance

Education
    Tuition & Fees
    Textbooks & Supplies
    Online Courses
    Student Loan Payments

Debt Payments
    Credit Card Payments
    Personal Loans
    Mortgage Extra Payment
    Other Debt Repayment

Savings & Investments
    Emergency Fund
    Retirement (401(k), IRA, etc.)
    Stocks/Bonds
    Savings Account
        
Entertainment
    Movies/Theater
    Concerts/Events
    Streaming Services
    Books & Magazines
    Hobbies & Crafts

Shopping
    Clothing & Footwear
    Electronics & Software
    Household Items
    Personal Care

Travel
    Airfare
    Lodging
    Car Rental
    Vacation Packages
    Travel Dining
    Gifts & Donations

Charitable Donations
    Gifts for Family & Friends
    Crowdfunding Contributions

Miscellaneous
    Pet Care
    Legal Fees
    Bank Fees
    Postage & Shipping
```
spend_track
├─ .git
│  ├─ COMMIT_EDITMSG
│  ├─ FETCH_HEAD
│  ├─ HEAD
│  ├─ ORIG_HEAD
│  ├─ branches
│  ├─ config
│  ├─ description
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  ├─ push-to-checkout.sample
│  │  └─ update.sample
│  ├─ index
│  ├─ info
│  │  └─ exclude
│  ├─ logs
│  │  ├─ HEAD
│  │  └─ refs
│  │     ├─ heads
│  │     │  └─ main
│  │     └─ remotes
│  │        └─ origin
│  │           ├─ HEAD
│  │           └─ main
│  ├─ objects
│  │  ├─ 00
│  │  │  └─ c7815beb83dbcac2f41a091ba6538f24751b5b
│  │  ├─ 04
│  │  │  └─ 1abfdc31da1f84da13e67e218e43dc1949bf85
│  │  ├─ 08
│  │  │  └─ e0c75f69def120d951781d1e976b63f26777ce
│  │  ├─ 0f
│  │  │  └─ b297a9c7d6ab3f18ae2e9636939e4e5ecc3357
│  │  ├─ 10
│  │  │  ├─ 29c06093fa937bfdbc9f31ecba011f094196d6
│  │  │  └─ c7494af639bbc9fb52cde866ed09beedc25350
│  │  ├─ 11
│  │  │  └─ fa06473cf91f699741de42b30d5175e619aa6f
│  │  ├─ 14
│  │  │  └─ 560628a281853547534b209e9d09610b2c9d82
│  │  ├─ 15
│  │  │  └─ edd6738d9006ab0d201b73d90e80a14fd12c0a
│  │  ├─ 17
│  │  │  └─ 5dc5e30304cd834ca64c79e4a360d57f1f71e2
│  │  ├─ 19
│  │  │  └─ 715f43a437a996711777043173a093ffd88ba2
│  │  ├─ 1a
│  │  │  ├─ 6f33161ff3048209250e2c1d52b67ea996aab0
│  │  │  ├─ 72135cd58010865d7b3f54efe1731d28fa6fed
│  │  │  └─ 9ff83a7c8251610edaf4138cf6c9d8862acade
│  │  ├─ 1b
│  │  │  └─ 6c81f0875acdadabf7a8811692cf23419f3dde
│  │  ├─ 1d
│  │  │  └─ 149ab550f8e5e3d4cefe4663852177ea02fcb8
│  │  ├─ 1e
│  │  │  └─ 720323a00255d822a0d908e6d5c9a4f52c778c
│  │  ├─ 1f
│  │  │  └─ 9fd44013e9d7919470cda13a40227501e79e96
│  │  ├─ 21
│  │  │  └─ dea6625f1ec0355569d57589ac34d65c0bc41d
│  │  ├─ 22
│  │  │  └─ 4f14ad63d9d5bce6769fe5bf3f5da35d904e38
│  │  ├─ 23
│  │  │  └─ 39a7bdd447696ec8fdac8a44b8fcd949fd247d
│  │  ├─ 25
│  │  │  └─ ed304732e29e60e14c4e3f8f5c6d13d6773572
│  │  ├─ 26
│  │  │  ├─ 7b55d1b479542201e890c020d7ce1b5444ccc0
│  │  │  └─ 94afa50611c5dc3b90a1931dc7bdb77f494a27
│  │  ├─ 27
│  │  │  └─ fb813945eb7a4c5f67f21bcefad722725de027
│  │  ├─ 28
│  │  │  ├─ b81a45b2f827eea39276bd1c11b3bb2acdfddf
│  │  │  └─ cd16e81f14e1ec78a0281b3ed4c2b874793cd0
│  │  ├─ 29
│  │  │  └─ 126ca0420460f7da9077bfadd2b12fd7097dfb
│  │  ├─ 2a
│  │  │  ├─ 3ae243e4c214e77e748d8b1cb29706c98ee0d9
│  │  │  └─ 6b0d7172b1f1550119069b779f00bf402e54fd
│  │  ├─ 2c
│  │  │  ├─ 8b26995e7c386b16157e943b9af95b59e1de25
│  │  │  └─ a19c225a33ad835fe83012ab8f7ced8888114c
│  │  ├─ 2d
│  │  │  ├─ 07462fcdf3fc72ebe17e0fc1c0934ec4338a0f
│  │  │  └─ 493e31465f707b0144c7818ce67fe38d65f4c3
│  │  ├─ 2f
│  │  │  └─ 517451496214073a527268bd91c3f1c0c27599
│  │  ├─ 31
│  │  │  └─ 8d44f0b88b42a5b26e45dbf07a22ecd14c24dd
│  │  ├─ 32
│  │  │  └─ 0d218aeffd26310158abe6d0276c1f9b7650c7
│  │  ├─ 34
│  │  │  ├─ 70e63c40e95cb758df1b2bca1a88d34fa5a4a5
│  │  │  └─ c927d936e7c493f998515739a0e9e5808a7543
│  │  ├─ 35
│  │  │  └─ 1cf887fcdad1b9208e99c791e9030eb21ecffb
│  │  ├─ 36
│  │  │  └─ 2ae4aa37fc98cd8a87ac68769518df4e9e3e6e
│  │  ├─ 38
│  │  │  └─ b8f0a237addaacb90865273a29dde0b8672582
│  │  ├─ 39
│  │  │  └─ 427fe7b92d5127a34f72b3b09ba3126d7a45a7
│  │  ├─ 3a
│  │  │  ├─ 1d0b1dd098fcc5a41a73f841441e14b65e28e1
│  │  │  └─ c1433e93661cb207cd2361e83dcb325a076f1f
│  │  ├─ 3b
│  │  │  └─ 71eb848e37625e421fb5b7c5e290bb32a3008e
│  │  ├─ 3c
│  │  │  └─ ff2549390e6b8347e1810ebd192f41debcba0c
│  │  ├─ 3f
│  │  │  └─ ca6e531f974382ad47011b0615ea9408e91c91
│  │  ├─ 42
│  │  │  └─ bdd359d535bb7f6eec3958ad10417b42512050
│  │  ├─ 43
│  │  │  └─ eb16916bee5c6f057570dcedd9f21e361fb302
│  │  ├─ 44
│  │  │  ├─ 6581ad585299d0fa749abe044da24131f5bdf2
│  │  │  └─ b5874d6cdec595e43270994ac44526b21d9575
│  │  ├─ 45
│  │  │  └─ 43e5b4d1642682535e1905c3e88f29bd6a6745
│  │  ├─ 48
│  │  │  ├─ 2918e7bb9936c357ac37bd1a9741d1b968ede9
│  │  │  ├─ 574d2ece21e241b88bc4f22d34e0f8c1af5472
│  │  │  └─ d320092bcdebf2c9938d13f4f70d12835fe5f7
│  │  ├─ 49
│  │  │  └─ 0e89941fb8b512dbfd8f1b4504d9e69b65d7e2
│  │  ├─ 4c
│  │  │  ├─ e1da2e86a460b5dd7c481e5fb33c4e0529c075
│  │  │  └─ fb27f905d3f6496dfbc78cf85eabda709d3a70
│  │  ├─ 4d
│  │  │  └─ 4da3b48eaa468fc02c6a9a1c553c79ae524c92
│  │  ├─ 4e
│  │  │  └─ 4b8704fbc7329a258913a5f6777d7b067425b9
│  │  ├─ 50
│  │  │  └─ 79dd2e61f4bf0eeefa49a91636eaa0554e0b69
│  │  ├─ 52
│  │  │  ├─ 8fdd681e2048042205306c251d181bc6fbf3d8
│  │  │  └─ eba3e8847f3bb9db8d6aeb4ecb5beea8876bf7
│  │  ├─ 53
│  │  │  └─ 1c5edc2bedb7162317440978c0ebd5fe44a101
│  │  ├─ 54
│  │  │  └─ 13fa9e0204b9988797cba0c9a098a9f017da71
│  │  ├─ 57
│  │  │  ├─ 03b551eb90b1d50cf2aeba59db12439e9915c5
│  │  │  └─ d499f71fabb2b5ee95997ebde9e8b4a64b6eae
│  │  ├─ 58
│  │  │  └─ 8748724d4667e42f89018856d1fb8dcd7aeabb
│  │  ├─ 59
│  │  │  └─ 9fe8a26847627151321c5111687f52cf14c3c2
│  │  ├─ 5a
│  │  │  └─ 11fd8eee9a92760652b18b6eaf02aaab2c2773
│  │  ├─ 5b
│  │  │  └─ 894f375a867869b6eb9a04e445e893479e9265
│  │  ├─ 62
│  │  │  ├─ 2ec1ecb4c9b0c66d66be9526a610c8a9e6c6f0
│  │  │  └─ 745c6ff5a3358dbb61c102c1283a95348ddd2d
│  │  ├─ 63
│  │  │  └─ 61b851c42b0f799bee804b870408d66cec4abc
│  │  ├─ 66
│  │  │  └─ c6027dfbf85587e08e0365c897926726c772be
│  │  ├─ 67
│  │  │  └─ b85ea0d4c18174662bb2c25fee8a7d59198d55
│  │  ├─ 6e
│  │  │  └─ 8cfd0f5fc9bf3cc69a625d841ad9905ccc541b
│  │  ├─ 73
│  │  │  └─ 9907d9e8da3961adb916bed52a5a5862709318
│  │  ├─ 76
│  │  │  └─ 8b9156e01c07d6ddd09f993e346d9b50fd6bcd
│  │  ├─ 78
│  │  │  └─ c311de76e2ceb0fbd07c7f58954236eebdaa5b
│  │  ├─ 79
│  │  │  └─ e24508f9a251bf0830e284d994ba377af41d68
│  │  ├─ 7a
│  │  │  ├─ 96ee2c32c56a80f87b48d7a02f2c7840166e75
│  │  │  └─ e5605a21f7e582eee3772a8252f847df3ea4c5
│  │  ├─ 7b
│  │  │  └─ 7eb56e8adb70f42e5208ae165af63d0b65ba05
│  │  ├─ 80
│  │  │  ├─ 43542e4fa85be19b8db588e5af4881e9cea0d6
│  │  │  └─ a627bf648b9289a62d434af83f84a547a8344e
│  │  ├─ 81
│  │  │  └─ 84b35b59933ee6f592fd03fa7a630e93ba3d07
│  │  ├─ 82
│  │  │  ├─ 2fd6b1c4ee0b0cb672036cb054bbbaf6ba0d73
│  │  │  └─ cf9bfed43abb665155a7fd6c4cba2fcdd08b1c
│  │  ├─ 83
│  │  │  └─ 9366c84806bb90bfb73b004e65868db70ec231
│  │  ├─ 84
│  │  │  └─ 49fa659ce82e9590d9777a09c86e3d24736c11
│  │  ├─ 85
│  │  │  ├─ 476a3c2eaa5102a7c4ed20c94d087674258119
│  │  │  └─ 64c67bd92ffb3ab8781157259f6b94ef7cac8b
│  │  ├─ 8a
│  │  │  └─ 2073ff7e0dda27d4be16cd9357d159334a77fc
│  │  ├─ 8b
│  │  │  └─ e69e032fc3052e956f2a1059e7b4423a1300ab
│  │  ├─ 8c
│  │  │  └─ de9d866fc9411e735ff13c0a77b07b998d537d
│  │  ├─ 8d
│  │  │  └─ dd9504a20831f7c6a3c6b16b2c1026bb440803
│  │  ├─ 90
│  │  │  ├─ 0fc7048a487eeae1ec699938757bd410ef5e89
│  │  │  └─ 618f8fd228400692f8d3cb73f0e00f747c7465
│  │  ├─ 92
│  │  │  └─ a4c4511843dde786b582068159c84c38c12ab9
│  │  ├─ 94
│  │  │  ├─ 5999c96aef95aa68e8e003fd6ade8834eaa42a
│  │  │  └─ 6d8a98a1b49f1cb7e2415aa50b5109f9fc0b25
│  │  ├─ 97
│  │  │  ├─ 52ebc042519f980d061a21548df4c9d232bb37
│  │  │  └─ d802e04c0b326b1e63941c2927f32d89492da5
│  │  ├─ 9b
│  │  │  └─ 77fa019245a038b0fd2e70c6991dcd357f611d
│  │  ├─ 9d
│  │  │  └─ f44a37d52d8faa0b0deb469e58b5129b27526b
│  │  ├─ 9e
│  │  │  └─ 93aa4269213ed8d8893f46fe6829b20e90e5ea
│  │  ├─ a0
│  │  │  └─ 6b20762ecd88bc9ee8d13ad96958f616702fcf
│  │  ├─ a2
│  │  │  └─ c9a7a40e0e8c015c8a90abdf9ac5984e413989
│  │  ├─ a3
│  │  │  └─ 4b4c239c99d44bbe2dd8908a07493c59b3e449
│  │  ├─ a4
│  │  │  └─ d93cf45869d58d32771a8816b71d7a410560c7
│  │  ├─ a5
│  │  │  └─ 6044698ce02c0d828f56806faadf531cae7d86
│  │  ├─ a7
│  │  │  └─ 19644ab7ce89c702adad74fb44e00b98f81eff
│  │  ├─ ab
│  │  │  └─ 4de09a706e2c89f83a5c946b0720dd3f1630f4
│  │  ├─ ad
│  │  │  ├─ 0a8087cd22190e33004317f45adc7860de1163
│  │  │  └─ 53d3e0f5069416a8ac0cdd22aad5f3970d7723
│  │  ├─ ae
│  │  │  └─ 13e83e0040b257c807d3fb2e3ec1c98fae4e56
│  │  ├─ af
│  │  │  └─ 046d8da95dea603b9f2137af2364e51b0a0f67
│  │  ├─ b1
│  │  │  └─ 7aab42ef8ade33e338a53a5e3147b161b584bb
│  │  ├─ b3
│  │  │  ├─ 2c2adf02c080442455b47c097dd15e33a6e783
│  │  │  └─ 76891db9bdf4dd2095ddd88a564ee8b47748be
│  │  ├─ b5
│  │  │  └─ 0f37637636308817205a7e8a395fc6350f5c83
│  │  ├─ b7
│  │  │  └─ 23105779a49ebbcdae1d07b4d754c7a63eaa2f
│  │  ├─ b9
│  │  │  └─ 1fb6bfcf2d87740f88ddeca4e75093234ca877
│  │  ├─ bb
│  │  │  ├─ 08bdc839e19b5d2cf75b575c3aa168dfb3b9f9
│  │  │  └─ 9d5793a33deacfce09e9f055415ece4836f6db
│  │  ├─ be
│  │  │  └─ 51fbe70684e4140ad54ff5dfef0586edbd9ae0
│  │  ├─ bf
│  │  │  └─ e49146d5b788eb0dd536730ee628304360ccd1
│  │  ├─ c1
│  │  │  └─ c8306e215d6f612a22939209fb39c8af87db1f
│  │  ├─ c4
│  │  │  └─ 86297ddccdfdf774fe9b8e0dc4584043b02652
│  │  ├─ c5
│  │  │  ├─ 219aab05e886cb779774a5cb268afdab6c2268
│  │  │  └─ f1930f83600a50b0702cc5d4457cec3e62c84f
│  │  ├─ c8
│  │  │  └─ cfafea3413e41f20e6a35b12f252571ef3d5a9
│  │  ├─ ca
│  │  │  └─ e07da0dbaecee731eaaeda86534896423c453c
│  │  ├─ cc
│  │  │  └─ 3c1954bdd960462b20eed212a6d6a9950cd2c7
│  │  ├─ cd
│  │  │  └─ a87080a5792e98d12adeb0c23c6900d54c9bc4
│  │  ├─ cf
│  │  │  ├─ 1ad884c6e5b5d433a79a3f2d2d5850357f6c93
│  │  │  ├─ 29474e219968bb67ce059ef3bae9538bc8e929
│  │  │  └─ f3d77933720f5d05feae8d3fe59f290a877400
│  │  ├─ d0
│  │  │  └─ 360d1c8c789e2f9f2e3ad6e7cf68781cdb8970
│  │  ├─ d2
│  │  │  └─ 540b33dd249892ea3089e4ec5283cbb532c48e
│  │  ├─ d3
│  │  │  ├─ b6def22a036aeb986e33e6da1db0289f20b7df
│  │  │  └─ d0e684ad88634906122389084f98cd2f24a4b4
│  │  ├─ d4
│  │  │  ├─ ce81a3227879ac74d570f5fc72dfd1cd0d9912
│  │  │  └─ f5b8d6bf1234c1d8456c8547138393709e94a9
│  │  ├─ d6
│  │  │  └─ 2f45b11a0b7f0511b829020cf934304285f7a7
│  │  ├─ d9
│  │  │  └─ 742e83d9aac16a3b42b9db65d48b32efa00b11
│  │  ├─ da
│  │  │  ├─ 5086b01926eec057bf99e0d89c19217486b2af
│  │  │  └─ 9b136619857959e55fa468e6baad54474e54b2
│  │  ├─ dc
│  │  │  ├─ 4b6af9420f49a3d11d974f17038e04a2751ba0
│  │  │  └─ 7ea67dfacb062a2c253ba20639ccdfc8cfceef
│  │  ├─ dd
│  │  │  └─ a7319f96ec83bf478ad8be324640c55a1c580d
│  │  ├─ df
│  │  │  └─ 8bc2beaf2a7586937e22d1647d43c9c532036e
│  │  ├─ e1
│  │  │  ├─ 94864b144fcb8e9574d49b452a35f40f05a2f4
│  │  │  └─ a015eb7981aec6aa420d3f9b0c376a1b1009a3
│  │  ├─ e2
│  │  │  └─ 9fd53456e5c74d3b1fb2e7cd6a008d872dac3e
│  │  ├─ e4
│  │  │  └─ ebf1a239f44b7d132f857ad960d9ddce3196bf
│  │  ├─ e5
│  │  │  └─ fd7342c8e29e525333afba6f74ccc273dc4dc0
│  │  ├─ e9
│  │  │  └─ ca295667024ebb56a6c29394a02629d41c276a
│  │  ├─ ea
│  │  │  └─ 9ecf605ad57a0bc4d959bf822ed5988c92c036
│  │  ├─ ee
│  │  │  └─ fd92a8fa30869bc8398293db1c701af83f6423
│  │  ├─ f2
│  │  │  ├─ 22154082bdd0f688409bb592933a7d6eb6987a
│  │  │  └─ 4fd90a09e1f964a5e5942307dac3f1ff4144fa
│  │  ├─ f4
│  │  │  └─ 00d8c4f1afcc486134bcfe0e563f280a2c611a
│  │  ├─ f7
│  │  │  └─ d1cbc3b8486f0d2a0f694cedbb33696b37125c
│  │  ├─ f8
│  │  │  └─ 15aee35800b23fb2b958264ce7fd6c1be92df3
│  │  ├─ fb
│  │  │  └─ bb058306970aac5b0e857239e94e19b9a6c646
│  │  ├─ fd
│  │  │  ├─ 332ffa6abf52442599528dd26a3b3f62e5e1d3
│  │  │  └─ 6123f87703ddccca5b9cfe272eb1e58e5b52a5
│  │  ├─ fe
│  │  │  └─ 190fee61e64714df21b143d842294ba2dcfce9
│  │  ├─ info
│  │  └─ pack
│  │     ├─ pack-425a44073997797844cc92284b298af77bc24d8c.idx
│  │     └─ pack-425a44073997797844cc92284b298af77bc24d8c.pack
│  ├─ packed-refs
│  └─ refs
│     ├─ heads
│     │  └─ main
│     ├─ remotes
│     │  └─ origin
│     │     ├─ HEAD
│     │     └─ main
│     └─ tags
├─ .gitignore
├─ README.md
├─ balance
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_transaction.py
│  │  ├─ 0003_transaction_current_balance.py
│  │  ├─ 0004_delete_transaction.py
│  │  ├─ 0005_delete_balance.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ category
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_subcategory.py
│  │  ├─ 0003_auto_20240210_1036.py
│  │  ├─ 0004_rename_expense_category_expensecategory.py
│  │  ├─ 0005_rename_expense_subcategory_expensesubcategory.py
│  │  ├─ 0006_incomecategory.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ core
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ expense
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_expense_subcategory.py
│  │  ├─ 0003_auto_20240115_2202.py
│  │  ├─ 0004_expense_methodofpayment.py
│  │  ├─ 0005_alter_expense_date.py
│  │  ├─ 0006_auto_20240129_2151.py
│  │  ├─ 0007_alter_expense_category.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ income
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ manage.py
├─ static
│  ├─ css
│  ├─ fonts
│  ├─ img
│  ├─ js
│  └─ style.css
├─ templates
│  ├─ balance
│  │  ├─ base.html
│  │  └─ index.html
│  ├─ base.html
│  ├─ category
│  │  ├─ add.html
│  │  ├─ addExpenseCategory.html
│  │  ├─ addIncomeCategory.html
│  │  └─ index.html
│  ├─ expense
│  │  ├─ 404.html
│  │  ├─ addExpense.html
│  │  ├─ delete.html
│  │  ├─ details.html
│  │  ├─ edit.html
│  │  └─ index.html
│  └─ income
│     ├─ add.html
│     ├─ delete.html
│     ├─ edit.html
│     ├─ index.html
│     └─ test.html
└─ user
   ├─ __init__.py
   ├─ admin.py
   ├─ apps.py
   ├─ migrations
   │  └─ __init__.py
   ├─ models.py
   ├─ tests.py
   └─ views.py

```