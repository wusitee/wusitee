Set-PSReadLineKeyHandler -Chord "Ctrl+f" -Function ForwardWord

#set the color

# enable z

Import-Module posh-git
oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\robbyrussell.omp.json" | Invoke-Expression
# Invoke-Expression (&starship init powershell)

Invoke-Expression (& { (lua C:/Scoop/apps/z.lua/current/z.lua --init powershell) -join "`n" })

Set-PSReadLineKeyHandler -Key "Tab" -Function MenuComplete

Set-PSReadlineKeyHandler -Key "Ctrl+d" -Function ViExit

Set-PSReadLineKeyHandler -Key "Ctrl+z" -Function Undo

# 1. 编译函数 make
function MakeThings {
	nmake.exe $args -nologo
}
Set-Alias -Name make -Value MakeThings

# Set-Alias -Name os-update -Value Update-Packages

# 3. 查看目录 ls & ll
function ListDirectory {
	(Get-ChildItem).Name
	Write-Host("")
}
Set-Alias -Name ls -Value ListDirectory
Set-Alias -Name ll -Value Get-ChildItem

function OpenCurrentFolder {
	param
	(
		$Path = '.'
	)
	Invoke-Item $Path
}
Set-Alias -Name open -Value OpenCurrentFolder
