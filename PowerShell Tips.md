POWERSHELL BEGINNER TIPS
=============================

### 参考资料

- [Microsoft PowerShell Docs](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-5.1)

- [PowerShell Gallery](https://www.powershellgallery.com/)



### 版本检查

```shell
> $PSVersionTable
```

如果 PSVersion 低于 5.1 的话，需要升级，否则对 PowerShell Gallery 支持不好

打开“控制面板 - 程序和功能 - 已安装更新”，检查是否有安装 Windows Management Framework。如果有，卸载更新。

下载 [WMF5.1](https://www.microsoft.com/en-us/download/details.aspx?id=54616)，安装。

 （友情提示：WMF 是作为 Windows 更新来卸载和安装的，非 常 慢 ……）



### 调试

检查权限

```shell
> Get-ExecutionPolicy
```

如果不是 RemoteSigned，切到 PowerShell(Admin)

```shell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

使用 PowerShell ISE

```shell
> which powershell_ise.exe
```

在 PowerShell ISE 选项中调整字号、字体到自己舒服的位置

ConEmu 新建标签页时可以自由选择 PowerShell 或者 PowerShell(Admin)，但默认启动还是建议 cmd，速度快很多



## TIPS

1) 检查选项是否可以 Pipeline 输入

```shell
> Get-Help -Name XXXX -Full
```

如果接受 ByValue 则可以

```shell
> "xxxx" | XXXX
```

如果接受 ByParameters 则需要 

```shell
> $obj = [PSCustomObject]@{<Param>='xxxx'}
> $obj | XXXX
```

2) Pipe 比循环快很多

3) 在函数和脚本中尽量使用 terminating error 和 try...catch 框架

4) 代码块：运行代码字符串

```shell
$newThing = { Write-Host "Hi! I am in a script block" }
& $newThing
```


# Excel 交互

```shell
param(
    [String]$xlsxfile
)

$targetSheet

$path = Get-Location
$xlsxfile = $path.Tostring() + "\" + $xlsxfile
Write-Host -ForegroundColor yellow "Opening $path" -BackgroundColor black

$ExcelObj = New-Object -comobject Excel.Application

Try {
    $WorkBook = $ExcelObj.Workbooks.Open($xlsxfile)
    Foreach ($Sheet in $WorkBook.Sheets) {
        If ($Sheet.Name -ne $targetSheet) {
            $Sheet.Delete()
        }
    }
    $Sheet = $WorkBook.Sheets.Item($targetSheet)

    $output = $path.Tostring() + "\output.xlsx"
    If (Test-Path $output) {
        Remove-Item $output
    }
    $WorkBook.SaveAs($output)
} Finally {
    $ExcelObj.Quit()
    Write-Host -ForegroundColor yellow "Done." -BackgroundColor black
}
```
