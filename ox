default partial alphanumeric_keys modifier_keys
xkb_symbols "ox" {

    name[Group1]= "English (Ox Standard)";

    // ` 0 1 2 3 4 5 6 7 8 9 | ^
    // % = [ ] { } @ < > ( ) \ $
    key <TLDE> {[ percent, grave ]};
    key <AE01> {[ equal, 0 ]};
    key <AE02> {[ bracketleft, 1 ]};
    key <AE03> {[ bracketright, 2 ]};
    key <AE04> {[ braceleft, 3 ]};
    key <AE05> {[ braceright, 4 ]};
    key <AE06> {[ at, 5 ]};
    key <AE07> {[ less, 6 ]};
    key <AE08> {[ greater, 7 ]};
    key <AE09> {[ parenleft, 8 ]};
    key <AE10> {[ parenright, 9 ]};
    key <AE11> {[ backslash, bar ]};
    key <AE12> {[ dollar, asciicircum ]};

    // Q W E R T Y U I O P _ * &
    // q w e r t y u i o p - + #
    key <AD01> {[ q,Q ]};
    key <AD02> {[ w,W ]};
    key <AD03> {[ e,E ]};
    key <AD04> {[ r,R ]};
    key <AD05> {[ t,T ]};
    key <AD06> {[ y,Y ]};
    key <AD07> {[ u,U ]};
    key <AD08> {[ i,I ]};
    key <AD09> {[ o,O ]};
    key <AD10> {[ p,P ]};
    key <AD11> {[ minus, underscore ]};
    key <AD12> {[ plus, asterisk ]};
    key <BKSL> {[ numbersign, ampersand ]};

    // A S D F G H J K L : "
    // a s d f g h j k l ; '
    key <AC01> {[ a, A ]};
    key <AC02> {[ s, S ]};
    key <AC03> {[ d, D ]};
    key <AC04> {[ f, F ]};
    key <AC05> {[ g, G ]};
    key <AC06> {[ h, H ]};
    key <AC07> {[ j, J ]};
    key <AC08> {[ k, K ]};
    key <AC09> {[ l, L ]};
    key <AC10> {[ semicolon, colon ]};
    key <AC11> {[ apostrophe, quotedbl ]};

    // Z X C V B N M ~ ! ?
    // z x c v b n m , . /
    key <AB01> {[ z, Z ]};
    key <AB02> {[ x, X ]};
    key <AB03> {[ c, C ]};
    key <AB04> {[ v, V ]};
    key <AB05> {[ b, B ]};
    key <AB06> {[ n, N ]};
    key <AB07> {[ m, M ]};
    key <AB08> {[ comma, asciitilde ]};
    key <AB09> {[ period, exclam ]};
    key <AB10> {[ slash, question ]};

    // Not sure if needed.
    // include "level3(ralt_switch)"
};

partial alphanumeric_keys modifier_keys
xkb_symbols "workox" {

    name[Group1]= "English (New Ox)";

    // $ 1 2 3 4 5 6 7 8 9 0 | `
    // ^ @ [ ] < > % { } ( ) \ =
    key <TLDE> {[ asciicircum, dollar ]};
    key <AE01> {[ at, 1 ]};
    key <AE02> {[ bracketleft, 2 ]};
    key <AE03> {[ bracketright, 3 ]};
    key <AE04> {[ less, 4 ]};
    key <AE05> {[ greater, 5 ]};
    key <AE06> {[ percent, 6 ]};
    key <AE07> {[ braceleft, 7 ]};
    key <AE08> {[ braceright, 8 ]};
    key <AE09> {[ parenleft, 9 ]};
    key <AE10> {[ parenright, 0 ]};
    key <AE11> {[ backslash, bar ]};
    key <AE12> {[ equal, grave ]};

    key <AD01> {[ colon, semicolon ]};
    key <AD02> {[ u, U ]};
    key <AD03> {[ r, R ]};
    key <AD04> {[ p, P ]};
    key <AD05> {[ x, X ]};
    key <AD06> {[ w, W ]};
    key <AD07> {[ f, F ]};
    key <AD08> {[ d, D ]};
    key <AD09> {[ h, H ]};
    key <AD10> {[ apostrophe, quotedbl ]};
    key <AD11> {[ minus, underscore ]};
    key <AD12> {[ plus, asterisk ]};
    key <BKSL> {[ numbersign, ampersand ]};

    key <AC01> {[ a, A ]};
    key <AC02> {[ e, E ]};
    key <AC03> {[ s, S ]};
    key <AC04> {[ t, T ]};
    key <AC05> {[ g, G ]};
    key <AC06> {[ b, B ]};
    key <AC07> {[ n, N ]};
    key <AC08> {[ l, L ]};
    key <AC09> {[ o, O ]};
    key <AC10> {[ i, I ]};
    key <AC11> {[ y, Y ]};

    key <AB01> {[ z, Z ]};
    key <AB02> {[ x, X ]};
    key <AB03> {[ c, C ]};
    key <AB04> {[ v, V ]};
    key <AB05> {[ q, Q ]};
    key <AB06> {[ k, K ]};
    key <AB07> {[ m, M ]};
    key <AB08> {[ comma, asciitilde ]};
    key <AB09> {[ period, exclam ]};
    key <AB10> {[ slash, question ]};
};

partial alphanumeric_keys modifier_keys
xkb_symbols "altox" {

    name[Group1]= "English (Alternate Ox)";

    // $ 1 2 3 4 5 6 7 8 9 0 | `
    // ^ @ [ ] < > % { } ( ) \ =
    key <TLDE> {[ asciicircum, dollar ]};
    key <AE01> {[ at, 1 ]};
    key <AE02> {[ bracketleft, 2 ]};
    key <AE03> {[ bracketright, 3 ]};
    key <AE04> {[ less, 4 ]};
    key <AE05> {[ greater, 5 ]};
    key <AE06> {[ percent, 6 ]};
    key <AE07> {[ braceleft, 7 ]};
    key <AE08> {[ braceright, 8 ]};
    key <AE09> {[ parenleft, 9 ]};
    key <AE10> {[ parenright, 0 ]};
    key <AE11> {[ backslash, bar ]};
    key <AE12> {[ equal, grave ]};

    // Y F R U W J P D O " _ * &
    // y f r u w j p d o ' - + #
    key <AD01> {[ y, Y ]};
    key <AD02> {[ f, F ]};
    key <AD03> {[ r, R ]};
    key <AD04> {[ u, U ]};
    key <AD05> {[ w, W ]};
    key <AD06> {[ j, J ]};
    key <AD07> {[ p, P ]};
    key <AD08> {[ d, D ]};
    key <AD09> {[ o, O ]};
    key <AD10> {[ apostrophe, quotedbl ]};
    key <AD11> {[ minus, underscore ]};
    key <AD12> {[ plus, asterisk ]};
    key <BKSL> {[ numbersign, ampersand ]};

    // A S H E G B N T L I ;
    // a s h e g b n t l i :
    key <AC01> {[ a, A ]};
    key <AC02> {[ s, S ]};
    key <AC03> {[ h, H ]};
    key <AC04> {[ e, E ]};
    key <AC05> {[ g, G ]};
    key <AC06> {[ b, B ]};
    key <AC07> {[ n, N ]};
    key <AC08> {[ t, T ]};
    key <AC09> {[ l, L ]};
    key <AC10> {[ i, I ]};
    key <AC11> {[ colon, semicolon ]};

    // Z X C V Q K M ~ ! ?
    // z x c v q k m , . /
    key <AB01> {[ z, Z ]};
    key <AB02> {[ x, X ]};
    key <AB03> {[ c, C ]};
    key <AB04> {[ v, V ]};
    key <AB05> {[ q, Q ]};
    key <AB06> {[ k, K ]};
    key <AB07> {[ m, M ]};
    key <AB08> {[ comma, asciitilde ]};
    key <AB09> {[ period, exclam ]};
    key <AB10> {[ slash, question ]};
};
