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



The command prompt that is presented on screen when you start PowerShell can be customized to your preferences. Many pieces of information can be added to the command prompt display to make it more useful. I recently invested some time to customize my command prompt with what I believe to be useful pieces of information. 启动PowerShell时屏幕上显示的命令提示符可以根据您的偏好进行定制。可以将许多信息添加到命令提示符显示中，以使其更有用。我最近花了一些时间用我认为有用的信息来定制命令提示符。

I would like to share with you how I customized my command prompt to display information such as the current folder and execution of the last command that was run. You can implement my customizations as is or you can create your own. Follow along and I will show you how I did it, then you will know how to make changes on your own. If you want to head straight to the finished code, just browse to the end of this post. 我想与您分享我是如何定制命令提示符来显示诸如当前文件夹和最后运行的命令的执行等信息的。您可以按原样实现我的自定义，也可以创建自己的自定义。跟着做，我将向你展示我是如何做到的，然后你就会知道如何自己做出改变。如果你想直接进入完成的代码，只要浏览到这篇文章的末尾。

# My Personal Preferences

Have your seen other community people present onscreen and you wondered how they got they command prompt to be so tricked out? Yeah, so did I... One day I decided I was going to figure out how to customize my command prompt to my liking. First thing I had to figure was, what did I want to see in my command prompt? 你有没有看到其他社区的人出现在屏幕上，你想知道他们是如何让他们的命令提示符如此花哨?是啊，我也是…有一天，我决定要弄清楚如何根据自己的喜好定制命令提示符。我必须弄清楚的第一件事是，我想在命令提示符中看到什么?

When I work on PowerShell scripts and commands, I have found there is a certain set of information that is beneficial for me to have at my fingertips. I like my PowerShell command prompt to give me information about my work environment. I customized my prompt so I don't have to try to remember what directory I am in or if I am running as administrator or not. Here's what my personalized command prompt looks like: 当我使用PowerShell脚本和命令时，我发现有一组信息对我很有用。我喜欢PowerShell命令提示符提供有关工作环境的信息。我定制了我的提示符，这样我就不必尝试记住我在哪个目录中，或者我是否以管理员身份运行。下面是我的个性化命令提示符:

My-Cmd-Prompt

There are six customizations in my command prompt that I will be covering. Let's go through the items and explain what they are.

My-Cmd-Prompt-by-Item-1

Item 1 displays if I am "running as administrator". This is sometimes referred to as "Elevated" or not. It disappears for non-elevated users.

Item 2 displays the current user that the command prompt is running as. I have multiple ID's I use to access resources and knowing which user is logged in as is helpful.

Item 3 displays the current folder I am in. It only displays the folder; not the entire path.

Item 4 is the time when the last command prompt was completed; it is not a live display of the current time. It will display what the current time was when the previous command finished executing. I use this as simple way to see what time I executed a command in the past.

Item 5 is the execution time (or runtime) of the last command. It displays the elapsed time in seconds or minutes, depending on how long the last command ran.

Item 6 shows the full path my command prompt is at. It shows the entire path.

I'm going to walk through each one of these items and show how each one is built. But before I can jump into the six items above, let's talk about what executes these settings.

The Prompt function
The information that is displayed when you launch PowerShell is configured by a built-in function called "Prompt". You can customize your command prompt by creating your own function called "Prompt" and saving your desired settings inside that function. You then add your "Prompt" function to your PowerShell profile and then your settings supersede the built-in prompt function.

The PowerShell profile is loaded every time you open a new command prompt and loads the code contained in the profile into memory. Once I cover all the individual pieces, I'll show how to configure your profile to run your customized prompt function. But first, let's get started going through the details of how to make the prompt look like my screenshot above.

Some information needed to customize the command prompt can be a bit complex and difficult to understand at first glance. I'll do my best to try to explain the code, but don't get down if you struggle with some of these code snippets. I pulled some of the snippets directly from Microsoft documentation. They don't need any modification at all to be used. If you understand what they do at a higher level, then that is enough for you to use this code in your script.

Detecting "Run as Administrator"
Looking back at the earlier screencap, the first piece of information displayed in the command prompt is if the command prompt is running "elevated". Elevation of privileges is a concept where the logged-in user should run with the lowest set of privileges, and they elevate their privileges (rights) when they need to change the system. Microsoft controls the process of elevating rights with User Access Control (aka UAC). If you want to modify your system from your PowerShell command prompt, then the PowerShell command prompt needs to be "elevated" (aka "Run As Administrator") in order to make changes.

The choice to elevate happens when you start the command prompt. If you start your day like me by opening a PowerShell command prompt and leave it open for an extended period, you may not remember if you were running elevated or not. The code to check for elevation is written in .NET and taken from the Microsoft website. There are many different uses of the same block of code online. The code checks the status of the identity that started the PS command prompt and reports if the identity is running under the "built-in administrator" role.

$IsAdmin = (New-Object Security.Principal.WindowsPrincipal ([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)
For all the code examples in this article, I save the results that I need to customize my command prompt to variables. I then assemble those variables later on with specific formatting to display the results as I wish. I am saving the result from the elevation query to a variable called $IsAdmin for later use. Also please note, that code snippet is the hardest bit of code to understand. they get easier to understand as we move farther along.

Displaying the Current User
I am reaching into .NET once again to find out what user is the command prompt running as. Don't confuse this with the previous query. The first query was checking to see if the user who started the console chose to elevate (aka Run As Administrator). This bit of code is querying which user started the command prompt.

If you have multiple ID's that you login as or if you run multiple command prompts at once, this piece of code is a great way to monitor which command prompt is running as which user.

 $CmdPromptUser = [Security.Principal.WindowsIdentity]::GetCurrent();
This snippet saves the current user of the console to a variable named $CmdPromptUser. I told you it would get easier. Let's move on to the next piece of the puzzle.

Displaying the Current Folder
I like to know what folder I am in, but displaying the full folder path inside my command prompt is problematic if I am working deep inside a set of nested folders. If I display the whole path, then my cursor may move all the way over to the right-most part of the console. By the time I type my commands, the line may wrap and make it difficult to read. I prefer to know the current folder I am in at all times, but I don't need to know the whole path; just the folder name.

PowerShell has an automatic variable called $PWD. This variable shows the complete path of the current directory. That path can be split apart using the Split-Path cmdlet. I can use the -leaf parameter to display only the current folder. In the example below, I have switched to my documents directory.

Display-the-current-folder

You can see that $PWD displays the full path. When I use the -leaf switch, it gives me just what I want: the folder name. I am saving the result to a variable named $CmdPromptCurrentFolder for later use.

$CmdPromptCurrentFolder = Split-Path -Path $pwd -Leaf
Creating a "timestamp" for commands
I often scroll back through my recent history to see commands I previously run. When I do that, I find it useful to have some sort of timestamp on my console that I can look back on and see approximately when commands were run. To do this, I display the current time when the previous command finished executing.

When the timestamp tweak is applied, the result is that the history now has a timestamp for all my previous commands display right there on the screen as I scroll back through my history. You can see in the screenshot below that I executed examples for this article over the course of a few hours. The timestamp helps me understand the history of commands better.

Time-Stamp-History

Creating a timestamp can be done by running Get-Date with some formatting syntax and returning the result to the screen. I am saving the result to a variable called $Date. Later on, I'll show where to use the $Date variable in the output.

$Date = Get-Date -Format 'dddd hh:mm:ss tt'
Querying how long the last command ran
Another helpful piece of information is knowing how long the last command I executed took to run. For most commands, the result ranges between a few milliseconds and a few seconds in length. Occasionally I will need to perform some queries that can run for multiple minutes before completing. Knowing how long command took to run is helpful and helps set a realistic expectation if I have to run a command again.

To get the last command, I query the history using Get-History and then instruct PowerShell to run only the last command.

 $LastCommand = Get-History -Count 1

The information available Get-History also includes how long a command took to run (execution time). If I run Get-History in PS7, I can use the duration property to show how long the last execution time was. But duration isn't an available property in PS5. I use PS5 and PS7, and I would like my code to work in both environments.

I can do some math to calculate duration and know that it will work in PS5 & PS7. Execution time is calculated by subtracting end time from the start time. Both of those values are included in the history for PS5 and PS7; you just need to know how to access the properties. I am saving the result displayed in seconds to a variable named $RunTime because that is the best value for most commands I run.

$RunTime = ($lastCommand.EndExecutionTime - $lastCommand.StartExecutionTime).TotalSeconds

Once the runtime is computed, we can customize the output. However, there is one unique scenario to deal with: The first time the console is launched. In that situation, there is no "last command". To account for that, I use an if loop to detect if there is a last command. If there is a last command, compute the run time. Otherwise do nothing. It might not be obvious in the code, but the if statement is testing true / false for $lastcommand. The command reads like this: "If $lastcommand exists (aka $true), calculate the value."

if ($lastCommand) { $RunTime = ($lastCommand.EndExecutionTime - $lastCommand.StartExecutionTime).TotalSeconds }

Recall earlier I mentioned that occasionally I have commands that take multiple minutes to complete. At some point, seconds becomes cumbersome when trying to understand length of time. For example, 286 seconds isn't easily converted in our heads to 4 minutes and 46 seconds. But we can design some code to convert seconds to minutes for long running queries.

In the syntax below, I am testing the total runtime. If it's greater than 60 seconds, the code converts the seconds to minutes and seconds. If it's not, then just display the time in seconds.

if ($RunTime -ge 60) {
    $ts = [timespan]::fromseconds($RunTime)
    $min, $sec = ($ts.ToString("mm\:ss")).Split(":")
    $ElapsedTime = -join ($min, " min ", $sec, " sec")
}
else {
    $ElapsedTime = [math]::Round(($RunTime), 2)
    $ElapsedTime = -join (($ElapsedTime.ToString()), " sec")
}

This block of code may seem a bit daunting at first, let me explain what is happening here. When I calculate the run time of the last command from the start and end exection times, I get the value in seconds. but when the value is over 60, I am asking PowerShell create a timespan, because I want to display the time differently for that scenario.

My goal is to be able to display the time in minutes and seconds. Since I start with seconds, I need to convert seconds to minutes and seconds and a timespan object does the work for me.

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


However, what I want to display is a string of text that prints the time on the screen, not actual time output. I have to convert the timespan to a string.

 $ts.ToString()
00:01:01.0119692


Now I have a string version of the time. But I only want minutes and seconds. I can get just the minutes and seconds by going one step further.

$ts.ToString("mm\:ss")
01:01


Now I have the time in minutes in seconds as a string. But I am still not done. I want to final output to look like this: [01 min 01 sec] . To do that, I need to split apart the time value into separate variables so I can append text in between. That happens with this line.

$min, $sec = ($ts.ToString("mm\:ss")).Split(":")


The line above splits the time output 01:01 into to two variables called $min and $sec . I can do that in one line by using the .split property and specify what to split on .Split(":"). PowerShell then deposits the two values into the two variables I specified. Now that I have two variables, I am using a -join statement to join the variables and some text to produce the output I desire [01 min 01 sec] . It seems like alot of code for a simple result, but I think the effort is worth the result.

if ($RunTime -ge 60) {
    $ts = [timespan]::fromseconds($RunTime)
    $min, $sec = ($ts.ToString("mm\:ss")).Split(":")
    $ElapsedTime = -join ($min, " min ", $sec, " sec")
}
Displaying the full folder path in the Title Bar
Earlier I mentioned that I only wanted the current folder name I am working in to be displayed in my PS command prompt. However, I also realize the value of seeing the whole path. That's why I stuck the full path in the title bar of the window to use as a reference that is out of the way but easy to find when I need it. You may prefer something different. The title bar has its own built-in variable $host.ui.RawUI.WindowTitle , I simply have to set it to my preference. I have added the words "Current Folder: " and the $pwd variable.

$host.ui.RawUI.WindowTitle = "Current Folder: $pwd"	
Bringing it all together
Let me show you how I brought the data together and formatted the output. Let's review, we have seven variables containing data: $IsAdmin,$CmdPromptUser,$CmdPromptCurrentFolder,$Date, $LastCommand, $RunTime, and $host.ui.RawUI.WindowTitle . What we need now is to display the data and format it to our preferences. Here's the code for the formatting


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
Many articles you read will say how terrible it is to use the Write-Host cmdlet for displaying data. This is because when you use Write-Host, the data is displayed on the screen and can't be reused. In our script, we're only using the data for display, so Write-Host or its newer version Write-Output is acceptable to use. That block of code is probably a bit confusing, so let's walk through each line and explain what is happening.

I am starting the formatting with a return of a blank line, this provides a little visual break from any previous commands. Then it is followed up with the formatting for the "elevated" info.

If the command prompted is elevated, then it will display the word "Elevated" with a red background. If not elevated, then nothing is displayed. This is controlled by the if/else statement. I use the -NoNewLine parameter at the end because I want to display the bits of information next to each other on the same line.

Write-Host ""
Write-Host ($(if ($IsAdmin) { 'Elevated ' } else { '' })) -BackgroundColor DarkRed -ForegroundColor White -NoNewline

Next is the formatting for displaying the current user info. I added the text "User: " to the output and use the .split property to get rid of the domain name and the slash. I have formatted this text with a blue background and once again use the -NoNewLine property to prevent a line break.

Write-Host " USER:$($CmdPromptUser.Name.split("\")[1]) " -BackgroundColor DarkBlue -ForegroundColor White -NoNewline

The next line displays the current folder. I spent a long time trying different color combinations and settled on Grey. I have added in some slashes to make the output look like a folder path. Once again, -NoNewLine is used to prevent a line break. By using -NoNewLine on this line of code along with the two previous lines, I have kept the Red, Blue and Grey blocks of text on one line.

Write-Host ".\$CmdPromptCurrentFolder\ "  -ForegroundColor White -BackgroundColor DarkGray -NoNewline

The last bit of information on the first line of text is the timestamp. This time I do not use the -NoNewLine property because I now want to start a new line after displaying the $date variable. Remember that I formatted the date to my preference when I saved the variable.

Write-Host " $date " -ForegroundColor White

The last piece of information being displayed is the $ElapsedTime variable. I added some simple formatting with brackets around the variable to make the output standout on the line. The last line starts with return and then displays the > symbol. The word return is a built-in function that tells the computer to exit the function. This is necessary so we can type at the command prompt and have it process the text as cmdlets and not as part of our function.

Write-Host "[$elapsedTime] " -NoNewline -ForegroundColor Green
return "> "

That covers all the individual pieces of the console customizations I used to configure the console prompt as I wish. The full script is listed below. You can add the script to your profile and when you launch PowerShell, you should have a customized command prompt.

If you're reading this post in a RSS reader, then you may not see the script listed at the bottom of article in your feed. The script is an embedded link to a github gist. If you can't see the script, then visit the post on my website and the script will be listed at the bottom.

If you want to see how I implemented this across multiple profiles, then take a look at the follow-up article which dives into where to save the code and how to have one customized profile for all users AND for BOTH PowerShell5 and PowerShell7. It walks you though the setup process in great detail.

Thanks for reading, I'd love to know what you think. Leave me a message in the comment section at the bottom of the page.



