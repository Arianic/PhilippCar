import cx_Freeze

executables = [cx_Freeze.Executable("catcarv2.py")]

cx_Freeze.setup(
    name="CatCar?",
    options={"build_exe": {"packages":["pygame", "time", "random"],
                           "include_files":["blood2.png", "blood4.png", "blood6.png", "capture4.png", "ela3.png", "sadface2.png", "background2.png", "sadface5.png", "crashmusic.wav", "backgroundmusic.wav", "menumusic.wav", ]}},
    executables = executables

    )
