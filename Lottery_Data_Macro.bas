Attribute VB_Name = "Module1"
Sub ltry_dta_macro()
Attribute ltry_dta_macro.VB_ProcData.VB_Invoke_Func = " \n14"
' ltry_dta_macro Macro
    Sheets("Initial Data").Select
    Columns("B:B").EntireColumn.AutoFit
    Columns("C:H").ColumnWidth = 13
    Range("A1:H1").Select
    With Selection.Interior
        .Pattern = xlSolid
        .PatternColorIndex = xlAutomatic
        .Color = 39372
        .TintAndShade = 0
        .PatternTintAndShade = 0
    End With
    Sheets("Averages").Select
    Columns("B:B").ColumnWidth = 22
    Columns("C:G").ColumnWidth = 18
    Range("A1:G1").Select
    With Selection.Interior
        .Pattern = xlSolid
        .PatternColorIndex = xlAutomatic
        .Color = 39372
        .TintAndShade = 0
        .PatternTintAndShade = 0
    End With
    Sheets("Advanced Statistics").Select
    Range("A1:C1").Select
    With Selection.Interior
        .Pattern = xlSolid
        .PatternColorIndex = xlAutomatic
        .Color = 39372
        .TintAndShade = 0
        .PatternTintAndShade = 0
    End With
    Columns("C:C").ColumnWidth = 18
End Sub
