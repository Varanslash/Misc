macro PythagoreanTheorem
    ld a, 3 ; main math thing
    ld d, a
    ld h, a ; counter
    dec h ; one less, to prevent off by one dragons
    ld b, 0 ; backup save
    .square\@
        add a, d ; add a to itself for multiplying
        dec h ; decrease counter
        ld b, a ; load main into backup
        ld a, h ; load counter into main for comparison
        cp a, 0 ; compare counter to 0
        ld a, b ; load backup back into main
        jr nz, .square\@ ; if counter is 0, jump
    ld e, a ; save for later
    ld a, 4 ; new number, can be anything
    ld d, a
    ld h, a
    dec h
    ld b, 0
    .square2\@
        ; copied cause logic is the same
        add a, d ; add a to itself for multiplying
        dec h ; decrease counter
        ld b, a ; load main into backup
        ld a, h ; load counter into main for comparison
        cp a, 0 ; compare counter to 0
        ld a, b ; load backup back into main
        jr nz, .square2\@
    add a, e
    ; a = c^2
    ld [$c000], a
endm
