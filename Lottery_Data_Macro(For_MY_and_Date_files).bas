Attribute VB_Name = "Module1"
Sub L_Dt_Macro()
Attribute L_Dt_Macro.VB_ProcData.VB_Invoke_Func = " \n14"
' Lottery Data Macro (Date-Based)
    Sheets("Initial Data").Select
    Range("A1:I1").Select
    With Selection.Interior
        .Pattern = xlSolid
        .PatternColorIndex = xlAutomatic
        .Color = 39372
        .TintAndShade = 0
        .PatternTintAndShade = 0
    End With
    Columns("A:A").ColumnWidth = 23
    With Selection
        .HorizontalAlignment = xlCenter
        .VerticalAlignment = xlTop
        .WrapText = True
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
    Sheets("Averages").Select
    Range("A1:G1").Select
    With Selection.Interior
        .Pattern = xlSolid
        .PatternColorIndex = xlAutomatic
        .Color = 39372
        .TintAndShade = 0
        .PatternTintAndShade = 0
    End With
    Columns("A:A").ColumnWidth = 23
    With Selection
        .HorizontalAlignment = xlCenter
        .VerticalAlignment = xlTop
        .WrapText = True
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
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
    Columns("A:A").ColumnWidth = 23
    With Selection
        .HorizontalAlignment = xlCenter
        .VerticalAlignment = xlTop
        .WrapText = True
        .Orientation = 0
        .AddIndent = False
        .IndentLevel = 0
        .ShrinkToFit = False
        .ReadingOrder = xlContext
        .MergeCells = False
    End With
End Sub
