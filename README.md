
# Hand-E

A robotic arm controlled via a Python script running on a microcontroller. Uses OpenCV & Mediapipe to visualize joints and uses trigonometric calculations for single-camera depth perception (SCDP) using pre-informed landmark nodes. Based on Tony Stark's Dum-E!




## Run the Visualization Script

The implementation for the two-vector system (TVS) for single-camera depth perception is **coming soon**.

Clone the project

```bash
  git clone https://github.com/aryan-cs/hand-e.git
```

Go to the project directory

```bash
  cd hand-e
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the program (Python will create a new window with a video stream)

```bash
  python main.py
```

## Conceptualization of SCDP using TVS

Currently, capturing from the 3-dimensional world to a 2-dimensional image results in information loss. Consistently calculating the angle between two distal phalanges, or fingertips, is impossible for generic movement due to the nature of the human movement. 

| Front-facing View | Side-facing View | Side-rotated View |
|     :---:      |     :---:      |     :---:      |
| ![Front-facing View](https://lh3.googleusercontent.com/pw/ABLVV87mhstnjihMCz4EVinAtFhgbtcIw81tEvO3Lp8i38D1dvaxPYEZXCso9pditwV4ZJcu_8_15m036LBl0cjNmS1LdwtkHGtqrvuJkmCA9RMrl5Sv6ZgKFya4hdWLnwEW82uzYdyfdjxUa47KX3QnbA-X7EtZcnPWOpbHoW5ERYAz840WksNvwlsT7arj5xdMcGALQ4Z9QIejdGfkyeJHKAF5pHtaCcWrwyjJL0i8ZEbHfsueEwxt4-5hFgyrfGiR7QV5luni6OqP53XjuLvOIMrDKZN-1c0FlN1CvJ8ANLBDHWhcWsPfDG2zsimnNx5F8zpspu7EiG7WGNbTANvUX0mcSOxsrke_JUnuARoj_EyWKZg-E6lbuCEFYscCPBNJjTsGq71Hs6Pdc-7UJX1-pAGl31EdyEmv8xykGSrPzNVGwLm5WqEKOD4Qc4S8RrU2IuKjjNnUuvP5nNn-u535Ea4a_V_OAEM3n_S2LhI_fYuBZlTqglWR6RZqJQGoLMEe8SfJeuMiFVoXkutRCMo8117CApHPUtJMZNnKuOb3riTkhHWj_k7PQ7cTlLSbWoZsxFkjNnr_opm2ilAa3UzekARiHIhk_5J9lIi2t8ssP1pb0cH98SERuP9Q-UM-LFqvpPgN875Yvlkyjl5onkrU5RCFQ5-HkqmL9DHt7OwbQI619s4xWnVD6yRvoDEgo6cbOz1QOeOREG7ZZIUX9h4o20gvSZzKxqydAXX-Jom3gLqv8yRvg1CHVzaU_d2pwCmqUaMKHZ0RtS2EB211fvWcdDUohp2fLMALHyXviySBO4hljGYZ-mehanw8CO6hTXxDwqX-PCUNopqQ7RuhVEqa7idMCVeUv7yBDx1_46TCvqiN4sHgLuZ4PhbmP7ExGZQxlg6B5qXo4QKFTLPzINm2VarwIw4sY3p-vOEWc3FRPtAcQIifMu2ZnS8NehLc1e_Ak19MH3tJUyfIcJG7_CXCzQwIGWw0Zx7NDDJSA51TCKaVlZnBB3NuS_Tv3VWHBeKw5zhu50F9YhvUGpP2MVDY6rvdfKE-gBKDmZ9hoCmn7kSqddwbhD4rpUUYlaOz25s0nIAxoqgaNu9TuWc1SQYwi4ZI5PjLbX9ufJEly_K1uDRMSRhxlbFUL2dXYA5Bu3Ouke_9esokt1NQFrK1JvdqDcTMGHzoTJTne0Jw8ueQ5mVr7SfDUbqtIit0aV1_lZbq1PSrXTqCeAotPlldQuKLdfCxsshXpEE2Fibr8R7w5FFd=w258-h194-no?authuser=0&quot) | ![Side-facing View](https://lh3.googleusercontent.com/pw/ABLVV84N20GlVbUTh0RcjfeW4u4L1XedXhWL_p3jgbCdB_U9jJ1klBR-279mVQWg8jw6NO8YeLt2GEUSi1C8dYfyYxxI8Y5gY3J5zngWn3mjgjLQd7v3EOf_AnKM4Se4jXkkzX-CrOAcCZf8BTb8mdN3k_8-OO7Fe_vAaQgnZooiS5XTU-7d9WneIoc8kL4l2ZLTm5QfdlB7px13yj1fCbVZ4UAl7jmtOEc0iqvET_mwKnTJbpSX2_Rs_N11-ralBhy0fpvczcgXTMHHA2pLjqhvXeo8Kq9ml-C2wmmJHNzr66oc6ZOkvdIk9KDv4aW677TgfCJUZ-WPJl51Tt2r9ne_gMECklChVNJTFgEIA9nhcbjB-4JTXyEpauCpuY3GxWv_acKngwIhsJG6fLZ7CF963_LC_ZnSv3bDeAgXjvHSxz8Xo3msL79Ms7XiI0fTiaLrmvXSjGHK5qFnvvc-NC95Eu_hCth8jRayeoZxiht9v4wzHEjO7TvGuhfKhDukPKcwVbV9_cNVHmkWc5WMtQPDooqCa3N_LesbQHjkhKtIfcjJpIDzv0d0AasEtaJzE8Ww-p6RauxaT08GkEq7Z0XH6gBnB8IeAm9wjWwIgk65LyyFBVQygBNlpUA5bqfFep0PH9_K_JkeyF6c6BVvNtQ9dZ0HryUuUOdeY1bFiqZdtuVQCf17cr8Dfd1Dg0UiJ_8CItT44kk3L4gkVPVJN9sAq0Q4zONRQPG_1IelznGpyi_5iGBYTMhJH4Xo9cCILcr7eLIpgvXGGyLvXnatim96oGeJYHqIkm7H69VNzWgwnm1bhZaFHiF6fmDJHzM7Ypw7todknS3WIY4da-rLcP9r-M0F2I_fSU9vGVBih-UCltfaY54T5NZcs5EycqGLgXoAHKmi9OnMatysKy1PuI3sUh4In8Y19el4M0hR2qSrggoNg4s69RssLV8EOM-n6nOYjkiWknT-lsvu7swQ4XCGNClAYyuudSjR_NIhQFtLJXri2rj3LPmt7rGr_aDE5SGkEHH0tfIYR7W0DKlFl2Nw1vxO3fhLNuSzFYeFEayvjvtpP_FnYM9dLS6SoACDfPlo9g14dmcNzv_VsalDk2inVidaKggV90DhiWyU7OkJ_KvR5fVKYxj0kWb2qf8RUNfCisfj05PZFwYf53a_X61Z3FuKhl3J5dC8pLQsc0mpKV0xIEWpz6NNnS7x0RcMX7LTCWv30X9WcikMiA7RMskH1y1ADC1pqr-yDCiIvOnZdmfs=w259-h194-no?authuser=0&quot) | ![Side-rotated View](https://lh3.googleusercontent.com/pw/ABLVV877D0-zR8kIRalA6fV3thsnTAO3_i4hr4AMiLm5mrCjLbO6yc8zFS1gEZD8u-WoTp7GzNQi7hyjvEby3_K5ECg3VUQEJG2NyPV2JDBPvzMdZ2h1h6Bk6DJ_0noiua6BKGZa1lDpenU3lqL3Y1HgRV_piDgkJSvqJ8TVzxrmqdPSQ4IbIA4OSYQ5hticwtEXjyCHkPjjD_HCURFXVa8TWYQvg7XaKnw5CqiM-uG_7pApzU8r-DQTp83fnRZZCCXXSOswtFRbJIhPmD9lVIxwhXFSktEc2NpXjK_QTxDWKokMcwCNgurVn1hmwcvie3z29UnY-N3IwuYx1iZehuMtm_igjQ-8UbaDjBlxS7GGeoK64zzVgdzeaqMcHuUu8LFD3Cj8D6W-DEXRQ6VFPY2tCJ7h0o7kUJe4B29p1BHVNcGFveDHyL8Vdks1ICqXZsd35BO78i03VIsLnGTx9CbjdR_c2amEwZmR6QNdN7lyXpBVQ6rbCrQ8x1zti0bN3Wb11sLO-4UhHBwNKjOsc2FURDs9p5hjoYnb-kYNygj9UtpHDmhTjHCrywfNdyko0yayC0jA__DAkPafOgw-DPWCGt8YE66Io4flm1QkEjcw73Sp2cUe3EupOxmRE3DcTOdwgNY6WKZMeggy9IFPulFz_42ummTlyjTghe_IZyy5UWj0TDU2TjgibD2qsYPnqQ76lQne_21ELZ9o8TisAtCIlPJBmiKO_k5IvGdlKeRwmafpfJnlIh0GStM7qQ6ZEtBrpCAMGk2NedPGPyzNLi3QqawmYJGoz2_I-UHJnPddd5kB7S1Lq_2oy_7UuZyeiies6nQGUIoHE7Xd4FqAy8YN_wDfcj0pokbJ13OsvilJLPWFVgq053N_2HZKuB8t-9viRJA6UTliAVnKtfsWX7MBDB_lOeWBvFPc9M8-r7SfRzv4w5ZQbR9EUa2V5sr6ugOYMQxrMIaPrNiD5CsX9_2YX5yi0IYtNGLPEDST02dVEQmnKqh3ZdyDGShGXwaZgfNpSuRG3y6syhdQG-Dv6jxhcGG0EDHahVBFW5wKsUllUfEo8ZVqDgpfpH8nQDMwGUI0uAdMVbLD1xTlI2IYuRquGeAiPwYdpFmJDFbea_s3y_ctqqzkfn--wUwHxkOGSwjrFPDZZrohaZg4hQBH6O8JoooqltfWPPcwLi5ct6L6AMX2yxxplQ4EaqFWlgnyot66XTY1veeDHgxdMokXwfj9HezSy4bNcV8ZdPusagVQX6x3=w260-h194-no?authuser=0&quot) |

Despite these photos capturing the same pose, the calculated distance between the index fingertip & thumb fingertip is different. To account for this, we can either use 3 cameras, one capturing each axis, or use other landmark nodes to gain context.

I propose a solution using the distance between the index finger base & little finger in conjunction with the information for the distance between the index-thumb fingertips. 

For the purposes of explanation, take the index-thumb vector to be a vector drawn from the distal phalanx of the index finger to the thumb. Take the index-little vector to be a vector drawn from the base of the index finger to the base of the little finger.

At all times, we have information on both the index-thumb vector and index-little vector. We can use the magnitudes of these vectors to calculate the angle at which the wrist is rotated given the maximum (90 degrees) and minimum (0 degrees). Using this information, we can interpret the magnitude of the index-thumb vector to understand whether the fingers are close together or far apart.




## Shortcomings of TVS

Information loss is inevitable when performing calculations for 3-dimensional processing on a 2-dimensional plane. In this case, we extend the domain of information by utilizing the index-thumb and index-length vectors, however, when viewing from the side-rotated view, it is impossible to correctly calculate the distance between the index and thumb fingertips. Here, we would either rely on a second perspective camera (preferably tangential to the existing viewpoint) or assume no change in index-thumb magnitude.

## Applications of TVS

The concept of SCDP can be extrapolated to full-body informed pose detection, such as understanding the direction a subject is facing (given the distance between shoulders or other landmarks). Due to the shortcomings of SCDP, however, it can only be applied in very specific scenarios where some level of mobility is expected to be controlled.
