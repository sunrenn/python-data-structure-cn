<!-- 

https://www.commandline.ninja/customize-pscmdprompt/

https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_prompts?view=powershell-7.3

https://www.jondjones.com/tactics/productivity/customise-your-powershell-prompt-like-a-boss/#:~:text=Customise%20Your%20Powershell%20Prompt%20Like%20A%20Boss%201,Status%20Info%20...%205%20Prettify%20The%20Terminal%20 


https://juejin.cn/post/7095370896822501390


-->

## 推荐了几个优化powershell的工具: 

- Oh My Posh
- Psreadline
- Terminal-Icons
- Pshosts



# HOW TO CUSTOMIZE YOUR POWERSHELL COMMAND PROMPT



The command prompt that is presented on screen when you start PowerShell can be customized to your preferences. Many pieces of information can be added to the command prompt display to make it more useful. I recently invested some time to customize my command prompt with what I believe to be useful pieces of information. 
启动PowerShell时屏幕上显示的命令提示符可以根据您的偏好进行定制。可以将许多信息添加到命令提示符显示中，以使其更有用。我最近花了一些时间用我认为有用的信息来定制命令提示符。

I would like to share with you how I customized my command prompt to display information such as the current folder and execution of the last command that was run. You can implement my customizations as is or you can create your own. Follow along and I will show you how I did it, then you will know how to make changes on your own. If you want to head straight to the finished code, just browse to the end of this post. 我想与您分享我是如何定制命令提示符来显示诸如当前文件夹和最后运行的命令的执行等信息的。您可以按原样实现我的自定义，也可以创建自己的自定义。跟着做，我将向你展示我是如何做到的，然后你就会知道如何自己做出改变。如果你想直接进入完成的代码，只要浏览到这篇文章的末尾。

# My Personal Preferences 我的个人喜好

Have your seen other community people present onscreen and you wondered how they got they command prompt to be so tricked out? Yeah, so did I... One day I decided I was going to figure out how to customize my command prompt to my liking. First thing I had to figure was, what did I want to see in my command prompt? 
你有没有看到其他社区的人出现在屏幕上，你想知道他们是如何让他们的命令提示符如此花哨?是啊，我也是…有一天，我决定要弄清楚如何根据自己的喜好定制命令提示符。我必须弄清楚的第一件事是，我想在命令提示符中看到什么?

> 我觉得就当前目录最有用, 还需要什么? 对了还有conda当前环境也应该保留.

When I work on PowerShell scripts and commands, I have found there is a certain set of information that is beneficial for me to have at my fingertips. I like my PowerShell command prompt to give me information about my work environment. I customized my prompt so I don't have to try to remember what directory I am in or if I am running as administrator or not. Here's what my personalized command prompt looks like: 
当我使用PowerShell脚本和命令时，我发现有一组信息对我很有用。我喜欢PowerShell命令提示符提供有关工作环境的信息。我定制了我的提示符，这样我就不必尝试记住我在哪个目录中，或者我是否以管理员身份运行。下面是我的个性化命令提示符:

![My-Cmd-Prompt.png](https://s2.loli.net/2023/10/12/gR6o2XYDzKI4qy7.png)

There are six customizations in my command prompt that I will be covering. Let's go through the items and explain what they are.

My-Cmd-Prompt-by-Item-1

- Item 1 displays if I am "running as administrator". This is sometimes referred to as "Elevated" or not. It disappears for non-elevated users.

- Item 2 displays the current user that the command prompt is running as. I have multiple ID's I use to access resources and knowing which user is logged in as is helpful.

- Item 3 displays the current folder I am in. It only displays the folder; not the entire path.

- Item 4 is the time when the last command prompt was completed; it is not a live display of the current time. It will display what the current time was when the previous command finished executing. I use this as simple way to see what time I executed a command in the past.

- Item 5 is the execution time (or runtime) of the last command. It displays the elapsed time in seconds or minutes, depending on how long the last command ran.

- Item 6 shows the full path my command prompt is at. It shows the entire path.

I'm going to walk through each one of these items and show how each one is built. But before I can jump into the six items above, let's talk about what executes these settings.

## The Prompt function

The information that is displayed when you launch PowerShell is configured by a built-in function called "Prompt". You can customize your command prompt by creating your own function called "Prompt" and saving your desired settings inside that function. You then add your "Prompt" function to your PowerShell profile and then your settings supersede the built-in prompt function. 启动PowerShell时显示的信息是由一个名为“Prompt”的内置函数配置的。您可以通过创建自己的名为“prompt”的函数并将所需设置保存在该函数中来定制命令提示符。然后将“提示”功能添加到PowerShell配置文件中，然后您的设置取代内置的提示功能。

The PowerShell profile is loaded every time you open a new command prompt and loads the code contained in the profile into memory. Once I cover all the individual pieces, I'll show how to configure your profile to run your customized prompt function. But first, let's get started going through the details of how to make the prompt look like my screenshot above. 每次打开一个新的命令提示符并将配置文件中包含的代码加载到内存中时，都会加载PowerShell配置文件。在介绍了所有单独的部分之后，我将展示如何配置您的概要文件以运行自定义的提示函数。但首先，让我们开始了解如何使提示看起来像我上面的截图的细节。

Some information needed to customize the command prompt can be a bit complex and difficult to understand at first glance. I'll do my best to try to explain the code, but don't get down if you struggle with some of these code snippets. I pulled some of the snippets directly from Microsoft documentation. They don't need any modification at all to be used. If you understand what they do at a higher level, then that is enough for you to use this code in your script. 定制命令提示符所需的一些信息可能有点复杂，乍一看很难理解。我将尽力解释这些代码，但如果您对其中一些代码片段感到困惑，请不要沮丧。我直接从微软文档中提取了一些片段。它们根本不需要任何修改就可以使用。如果您了解它们在更高级别上的作用，那么您就可以在脚本中使用这些代码。

## Detecting "Run as Administrator"

Looking back at the earlier screencap, the first piece of information displayed in the command prompt is if the command prompt is running "elevated". Elevation of privileges is a concept where the logged-in user should run with the lowest set of privileges, and they elevate their privileges (rights) when they need to change the system. Microsoft controls the process of elevating rights with User Access Control (aka UAC). If you want to modify your system from your PowerShell command prompt, then the PowerShell command prompt needs to be "elevated" (aka "Run As Administrator") in order to make changes. 回顾前面的屏幕截图，命令提示符中显示的第一条信息是命令提示符是否正在运行“elevated”。特权提升是一个概念，在这个概念中，登录用户应该以最低的特权集运行，当他们需要更改系统时，他们会提升自己的特权(权限)。微软通过用户访问控制(又名UAC)控制提升权限的过程。如果你想从PowerShell命令提示符修改你的系统，那么PowerShell命令提示符需要被“提升”(又名“以管理员身份运行”)，以便进行修改。

The choice to elevate happens when you start the command prompt. If you start your day like me by opening a PowerShell command prompt and leave it open for an extended period, you may not remember if you were running elevated or not. The code to check for elevation is written in .NET and taken from the Microsoft website. There are many different uses of the same block of code online. The code checks the status of the identity that started the PS command prompt and reports if the identity is running under the "built-in administrator" role. 在启动命令提示符时选择提升。如果您像我一样打开PowerShell命令提示符并长时间打开它，那么您可能不记得自己是否运行了升级。检查提升的代码是用 .net 编写的，取自Microsoft网站。同一段代码有许多不同的用法。代码检查启动PS命令提示符的标识的状态，并报告该标识是否在“内置管理员”角色下运行。

```bash
$IsAdmin = (New-Object Security.Principal.WindowsPrincipal ([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)
```

For all the code examples in this article, I save the results that I need to customize my command prompt to variables. I then assemble those variables later on with specific formatting to display the results as I wish. I am saving the result from the elevation query to a variable called $IsAdmin for later use. Also please note, that code snippet is the hardest bit of code to understand. they get easier to understand as we move farther along. 对于本文中的所有代码示例，我保存了将命令提示符定制为变量所需的结果。然后，我稍后用特定的格式组合这些变量，以按我希望的方式显示结果。我将提升查询的结果保存到一个名为$IsAdmin的变量中以供以后使用。还请注意，该代码片段是最难理解的代码。随着我们的深入，它们变得更容易理解。

## Displaying the Current User

I am reaching into .NET once again to find out what user is the command prompt running as. Don't confuse this with the previous query. The first query was checking to see if the user who started the console chose to elevate (aka Run As Administrator). This bit of code is querying which user started the command prompt.

If you have multiple ID's that you login as or if you run multiple command prompts at once, this piece of code is a great way to monitor which command prompt is running as which user.
```bash
$CmdPromptUser = [Security.Principal.WindowsIdentity]::GetCurrent();
```
This snippet saves the current user of the console to a variable named $CmdPromptUser. I told you it would get easier. Let's move on to the next piece of the puzzle.

Displaying the Current Folder
I like to know what folder I am in, but displaying the full folder path inside my command prompt is problematic if I am working deep inside a set of nested folders. If I display the whole path, then my cursor may move all the way over to the right-most part of the console. By the time I type my commands, the line may wrap and make it difficult to read. I prefer to know the current folder I am in at all times, but I don't need to know the whole path; just the folder name.

PowerShell has an automatic variable called $PWD. This variable shows the complete path of the current directory. That path can be split apart using the Split-Path cmdlet. I can use the -leaf parameter to display only the current folder. In the example below, I have switched to my documents directory.

## Display-the-current-folder

You can see that $PWD displays the full path. When I use the -leaf switch, it gives me just what I want: the folder name. I am saving the result to a variable named $CmdPromptCurrentFolder for later use.

```bash
$CmdPromptCurrentFolder = Split-Path -Path $pwd -Leaf
```

## Creating a "timestamp" for commands

I often scroll back through my recent history to see commands I previously run. When I do that, I find it useful to have some sort of timestamp on my console that I can look back on and see approximately when commands were run. To do this, I display the current time when the previous command finished executing. 我经常翻回最近的历史记录，查看我以前运行的命令。当我这样做时，我发现在控制台上有某种时间戳是很有用的，我可以回顾并大致了解命令是何时运行的。为此，我将显示前一个命令完成执行的当前时间。

When the timestamp tweak is applied, the result is that the history now has a timestamp for all my previous commands display right there on the screen as I scroll back through my history. You can see in the screenshot below that I executed examples for this article over the course of a few hours. The timestamp helps me understand the history of commands better. 当应用时间戳调整时，结果是，当我回滚历史记录时，历史记录现在有了我以前所有命令的时间戳，显示在屏幕上。您可以在下面的截图中看到，我在几个小时的时间里为本文执行了一些示例。时间戳帮助我更好地理解命令的历史。

### Time-Stamp-History

Creating a timestamp can be done by running Get-Date with some formatting syntax and returning the result to the screen. I am saving the result to a variable called $Date. Later on, I'll show where to use the $Date variable in the output.

```bash
$Date = Get-Date -Format 'dddd hh:mm:ss tt'
```

### Querying how long the last command ran

Another helpful piece of information is knowing how long the last command I executed took to run. For most commands, the result ranges between a few milliseconds and a few seconds in length. Occasionally I will need to perform some queries that can run for multiple minutes before completing. Knowing how long command took to run is helpful and helps set a realistic expectation if I have to run a command again. 另一个有用的信息是知道我执行的最后一个命令运行了多长时间。对于大多数命令，结果的长度在几毫秒到几秒之间。有时，我需要执行一些查询，这些查询在完成之前可能会运行数分钟。知道运行命令所需的时间是有帮助的，并且在必须再次运行命令时有助于设置一个现实的期望。

To get the last command, I query the history using Get-History and then instruct PowerShell to run only the last command. 为了获得最后一条命令，我使用get - history查询历史记录，然后指示PowerShell只运行最后一条命令。

```bash
$LastCommand = Get-History -Count 1
```

The information available Get-History also includes how long a command took to run (execution time). If I run Get-History in PS7, I can use the duration property to show how long the last execution time was. But duration isn't an available property in PS5. I use PS5 and PS7, and I would like my code to work in both environments. 可用的Get-History信息还包括命令运行所需的时间(执行时间)。如果我在PS7中运行Get-History，我可以使用duration属性来显示最后一次执行时间的长度。但在PS5中，持续时间不是一个可用的属性。我使用PS5和PS7，我希望我的代码在这两个环境中都能工作。

I can do some math to calculate duration and know that it will work in PS5 & PS7. Execution time is calculated by subtracting end time from the start time. Both of those values are included in the history for PS5 and PS7; you just need to know how to access the properties. I am saving the result displayed in seconds to a variable named $RunTime because that is the best value for most commands I run. 我可以做一些数学计算来计算持续时间，并知道它将适用于PS5和PS7。执行时间由开始时间减去结束时间计算。这两个值都包含在PS5和PS7的历史中;您只需要知道如何访问属性。我将以秒为单位显示的结果保存到一个名为$RunTime的变量中，因为这是我运行的大多数命令的最佳值。

```bash
$RunTime = ($lastCommand.EndExecutionTime - $lastCommand.StartExecutionTime).TotalSeconds
```

Once the runtime is computed, we can customize the output. However, there is one unique scenario to deal with: The first time the console is launched. In that situation, there is no "last command". To account for that, I use an if loop to detect if there is a last command. If there is a last command, compute the run time. Otherwise do nothing. It might not be obvious in the code, but the if statement is testing true / false for $lastcommand. The command reads like this: "If $lastcommand exists (aka $true), calculate the value." 计算完运行时后，我们可以自定义输出。然而，有一个独特的场景需要处理:第一次启动控制台。在这种情况下，没有“最后的命令”。为了解决这个问题，我使用if循环来检测是否有最后一个命令。如果有最后一个命令，计算运行时间。否则什么都不做。在代码中可能不太明显，但是if语句正在测试$lastcommand的true / false。该命令是这样读的:“如果$lastcommand存在(也就是$true)，计算其值。”

```bahs
if ($lastCommand) { $RunTime = ($lastCommand.EndExecutionTime - $lastCommand.StartExecutionTime).TotalSeconds }
```

Recall earlier I mentioned that occasionally I have commands that take multiple minutes to complete. At some point, seconds becomes cumbersome when trying to understand length of time. For example, 286 seconds isn't easily converted in our heads to 4 minutes and 46 seconds. But we can design some code to convert seconds to minutes for long running queries. 回想一下前面我提到过的，有时我的命令需要花好几分钟才能完成。在某种程度上，当试图理解时间的长度时，秒变得很麻烦。例如，286秒在我们的头脑中很难转换成4分46秒。但是我们可以设计一些代码，将长时间运行的查询的秒转换为分钟。

In the syntax below, I am testing the total runtime. If it's greater than 60 seconds, the code converts the seconds to minutes and seconds. If it's not, then just display the time in seconds. 在下面的语法中，我将测试整个运行时。如果大于60秒，代码将秒转换为分钟和秒。如果不是，那么就以秒为单位显示时间


if ($RunTime -ge 60) {
    $ts = [timespan]::fromseconds($RunTime)
    $min, $sec = ($ts.ToString("mm\:ss")).Split(":")
    $ElapsedTime = -join ($min, " min ", $sec, " sec")
}
else {
    $ElapsedTime = [math]::Round(($RunTime), 2)
    $ElapsedTime = -join (($ElapsedTime.ToString()), " sec")
}

This block of code may seem a bit daunting at first, let me explain what is happening here. When I calculate the run time of the last command from the start and end exection times, I get the value in seconds. but when the value is over 60, I am asking PowerShell create a timespan, because I want to display the time differently for that scenario. 这段代码一开始可能看起来有点吓人，让我来解释一下这里发生了什么。当我从开始和结束执行时间计算最后一个命令的运行时间时，我得到了以秒为单位的值。但是当值超过60时，我要求PowerShell创建一个时间跨度，因为我想在这种情况下以不同的方式显示时间。

My goal is to be able to display the time in minutes and seconds. Since I start with seconds, I need to convert seconds to minutes and seconds and a timespan object does the work for me. 我的目标是能够以分和秒来显示时间。因为我从秒开始，所以我需要将秒转换为分钟和秒，而时间跨度对象可以为我完成这项工作。

$ts

Days              : 0
Hours             : 0
Minutes           : 1
Seconds           : 1
Milliseconds      : 11
Ticks             : 610119692
TotalDays         : 0.000706157050925926
TotalHours        : 0.0169477692222222
TotalMinutes      : 1.01686615333333
TotalSeconds      : 61.0119692
TotalMilliseconds : 61011.9692


However, what I want to display is a string of text that prints the time on the screen, not actual time output. I have to convert the timespan to a string. 但是，我想要显示的是在屏幕上打印时间的文本字符串，而不是实际的时间输出。我必须将时间跨度转换为字符串。

```bash
$ts.ToString()
00:01:01.0119692
```


Now I have a string version of the time. But I only want minutes and seconds. I can get just the minutes and seconds by going one step further. 现在我有了一个字符串版本的时间。但我只想要分和秒。再往前走一步，我就能得到分和秒。

```bash
$ts.ToString("mm\:ss")
01:01
```

Now I have the time in minutes in seconds as a string. But I am still not done. I want to final output to look like this: [01 min 01 sec] . To do that, I need to split apart the time value into separate variables so I can append text in between. That happens with this line. 现在我有了以分钟和秒为单位的时间字符串。但我还没说完。我希望最终输出看起来像这样:[01分01秒]。为此，我需要将时间值拆分为单独的变量，以便在其中添加文本。这条直线也是这样。

```bash
$min, $sec = ($ts.ToString("mm\:ss")).Split(":")
```


The line above splits the time output 01:01 into to two variables called $min and $sec . I can do that in one line by using the .split property and specify what to split on .Split(":"). PowerShell then deposits the two values into the two variables I specified. Now that I have two variables, I am using a -join statement to join the variables and some text to produce the output I desire [01 min 01 sec] . It seems like alot of code for a simple result, but I think the effort is worth the result. 上面这行代码将时间输出01:01分成两个变量，分别是$min和$sec。我可以在一行中使用。split属性并指定在。split(":")上分割的内容。PowerShell然后将这两个值存入我指定的两个变量中。现在我有了两个变量，我将使用-join语句将变量和一些文本连接起来，以产生我想要的输出[01 min 01 sec]。看起来为了一个简单的结果编写了很多代码，但我认为付出的努力是值得的。

```bash
if ($RunTime -ge 60) {
    $ts = [timespan]::fromseconds($RunTime)
    $min, $sec = ($ts.ToString("mm\:ss")).Split(":")
    $ElapsedTime = -join ($min, " min ", $sec, " sec")
}
```

## Displaying the full folder path in the Title Bar

Earlier I mentioned that I only wanted the current folder name I am working in to be displayed in my PS command prompt. However, I also realize the value of seeing the whole path. That's why I stuck the full path in the title bar of the window to use as a reference that is out of the way but easy to find when I need it. You may prefer something different. The title bar has its own built-in variable $host.ui.RawUI.WindowTitle , I simply have to set it to my preference. I have added the words "Current Folder: " and the $pwd variable. 前面我提到，我只希望在PS命令提示符中显示我正在使用的当前文件夹名称。然而，我也意识到看到整个路径的价值。这就是为什么我把完整的路径放在窗口的标题栏中，作为一个参考，虽然不太显眼，但在我需要的时候很容易找到。你可能更喜欢不同的东西。标题栏有它自己的内置变量$host.ui.RawUI。WindowTitle，我只需要把它设为我的首选项。我添加了单词“当前文件夹:”和$pwd变量。

```bash
$host.ui.RawUI.WindowTitle = "Current Folder: $pwd"	
```

## Bringing it all together
Let me show you how I brought the data together and formatted the output. Let's review, we have seven variables containing data: $IsAdmin,$CmdPromptUser,$CmdPromptCurrentFolder,$Date, $LastCommand, $RunTime, and $host.ui.RawUI.WindowTitle . What we need now is to display the data and format it to our preferences. Here's the code for the formatting 让我向您展示如何将数据组合在一起并格式化输出。让我们回顾一下，我们有7个包含数据的变量:$IsAdmin，$CmdPromptUser，$CmdPromptCurrentFolder，$Date， $LastCommand， $RunTime和$host.ui.RawUI。WindowTitle。我们现在需要的是显示数据并按照我们的偏好格式化它。下面是格式化的代码

```bash
#Decorate the CMD Prompt
Write-Host ""
Write-Host ($(if ($IsAdmin) { 'Elevated ' } else { '' })) -BackgroundColor DarkRed -ForegroundColor White -NoNewline
Write-Host " USER:$($CmdPromptUser.Name.split("\")[1]) " -BackgroundColor DarkBlue -ForegroundColor White -NoNewline
If ($CmdPromptCurrentFolder -like "*:*")
        {Write-Host " $CmdPromptCurrentFolder "  -ForegroundColor White -BackgroundColor DarkGray -NoNewline}
        else {Write-Host ".\$CmdPromptCurrentFolder\ "  -ForegroundColor White -BackgroundColor DarkGray -NoNewline}
Write-Host " $date " -ForegroundColor White
Write-Host "[$elapsedTime] " -NoNewline -ForegroundColor Green
return "> "
```

Many articles you read will say how terrible it is to use the Write-Host cmdlet for displaying data. This is because when you use Write-Host, the data is displayed on the screen and can't be reused. In our script, we're only using the data for display, so Write-Host or its newer version Write-Output is acceptable to use. That block of code is probably a bit confusing, so let's walk through each line and explain what is happening. 您读过的许多文章都会说，使用Write-Host cmdlet显示数据是多么糟糕。这是因为在使用Write-Host时，数据显示在屏幕上，不能重用。在我们的脚本中，我们只使用用于显示的数据，因此可以使用Write-Host或其更新版本Write-Output。这段代码可能有点令人困惑，所以让我们遍历每一行并解释发生了什么。

I am starting the formatting with a return of a blank line, this provides a little visual break from any previous commands. Then it is followed up with the formatting for the "elevated" info. 我从返回空行开始格式化，这与之前的命令有一点视觉上的区别。然后，对“提升”信息进行格式化。

If the command prompted is elevated, then it will display the word "Elevated" with a red background. If not elevated, then nothing is displayed. This is controlled by the if/else statement. I use the -NoNewLine parameter at the end because I want to display the bits of information next to each other on the same line. 如果命令提示被提升，那么它将显示带有红色背景的单词“elevated”。如果未升高，则不显示任何内容。这是由if/else语句控制的。我在最后使用了-NoNewLine 参数，因为我想在同一行上相邻地显示信息位。

```bash
Write-Host ""
Write-Host ($(if ($IsAdmin) { 'Elevated ' } else { '' })) -BackgroundColor DarkRed -ForegroundColor White -NoNewline
```

Next is the formatting for displaying the current user info. I added the text "User: " to the output and use the .split property to get rid of the domain name and the slash. I have formatted this text with a blue background and once again use the -NoNewLine property to prevent a line break. 接下来是显示当前用户信息的格式化。我将文本“User:”添加到输出中，并使用.split属性来删除域名和斜杠。我用蓝色背景格式化了这个文本，并再次使用-NoNewLine属性来防止换行。

```bash
Write-Host " USER:$($CmdPromptUser.Name.split("\")[1]) " -BackgroundColor DarkBlue -ForegroundColor White -NoNewline
```

The next line displays the current folder. I spent a long time trying different color combinations and settled on Grey. I have added in some slashes to make the output look like a folder path. Once again, -NoNewLine is used to prevent a line break. By using -NoNewLine on this line of code along with the two previous lines, I have kept the Red, Blue and Grey blocks of text on one line. 下一行显示当前文件夹。我花了很长时间尝试不同的颜色组合，最后选定了灰色。我添加了一些斜杠，使输出看起来像一个文件夹路径。同样，-NoNewLine用于防止换行。通过在这行代码和前两行代码中使用-NoNewLine，我将红色、蓝色和灰色的文本块保留在一行上。

```bash
Write-Host ".\$CmdPromptCurrentFolder\ "  -ForegroundColor White -BackgroundColor DarkGray -NoNewline
```

The last bit of information on the first line of text is the timestamp. This time I do not use the -NoNewLine property because I now want to start a new line after displaying the $date variable. Remember that I formatted the date to my preference when I saved the variable. 
文本第一行的最后一位信息是时间戳。这次我没有使用-NoNewLine属性，因为我现在想在显示$date变量之后开始一个新行。记住，在保存变量时，我按照自己的偏好格式化了日期。

```bash
Write-Host " $date " -ForegroundColor White
```

The last piece of information being displayed is the $ElapsedTime variable. I added some simple formatting with brackets around the variable to make the output standout on the line. The last line starts with return and then displays the > symbol. The word return is a built-in function that tells the computer to exit the function. This is necessary so we can type at the command prompt and have it process the text as cmdlets and not as part of our function.
显示的最后一条信息是$ElapsedTime变量。我在变量周围添加了一些简单的格式，用括号括起来，使输出在行中更加突出。最后一行以return开头，然后显示&gt;的象征。单词return是一个内置函数，它告诉计算机退出该函数。这是必要的，这样我们就可以在命令提示符下输入，并让它作为cmdlet处理文本，而不是作为函数的一部分。

```bash
Write-Host "[$elapsedTime] " -NoNewline -ForegroundColor Green
return "> "
```

That covers all the individual pieces of the console customizations I used to configure the console prompt as I wish. The full script is listed below. You can add the script to your profile and when you launch PowerShell, you should have a customized command prompt.
这涵盖了我用来按照自己的意愿配置控制台提示符的控制台自定义的所有单独部分。完整的脚本如下所示。您可以将该脚本添加到您的配置文件中，当启动PowerShell时，您应该有一个自定义的命令提示符。

If you're reading this post in a RSS reader, then you may not see the script listed at the bottom of article in your feed. The script is an embedded link to a github gist. If you can't see the script, then visit the post on my website and the script will be listed at the bottom.
如果你在RSS阅读器中阅读这篇文章，那么你可能不会在你的订阅中看到文章底部列出的脚本。该脚本是指向github要点的嵌入式链接。如果你不能看到脚本，然后访问我的网站上的帖子，脚本将在底部列出。

If you want to see how I implemented this across multiple profiles, then take a look at the follow-up article which dives into where to save the code and how to have one customized profile for all users AND for BOTH PowerShell5 and PowerShell7. It walks you though the setup process in great detail.
如果您想了解我是如何跨多个配置文件实现这一点的，那么请查看后续文章，该文章深入研究了在哪里保存代码以及如何为所有用户以及PowerShell5和PowerShell7创建一个自定义配置文件。它将非常详细地指导您完成设置过程。

Thanks for reading, I'd love to know what you think. Leave me a message in the comment section at the bottom of the page. 
谢谢你的阅读，我很想知道你的想法。请在页面底部的评论区给我留言。



```bash
# 修改提示符的方式就是重新定义一个内部函数`prompt`, 不区分大小写.
# 按理说把下面的代码塞进~/.profile里应该有效果啊


function Prompt {
    #Decorate the CMD Prompt
    #Decorate the CMD Prompt
    Write-Host ""
    Write-Host ($(if ($IsAdmin) { 'Elevated ' } else { '' })) -BackgroundColor DarkRed -ForegroundColor White -NoNewline
    Write-Host " USER:$($CmdPromptUser.Name.split("\")[1]) " -BackgroundColor DarkBlue -ForegroundColor White -NoNewline
    If ($CmdPromptCurrentFolder -like "*:*")
            {Write-Host " $CmdPromptCurrentFolder "  -ForegroundColor White -BackgroundColor DarkGray -NoNewline}
            else {Write-Host ".\$CmdPromptCurrentFolder\ "  -ForegroundColor White -BackgroundColor DarkGray -NoNewline}
    Write-Host " $date " -ForegroundColor White
    Write-Host "[$elapsedTime] " -NoNewline -ForegroundColor Green
    return "> "

}
function prompt {$null}



```