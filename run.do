######################################################################
#
# 文件名称 : run.do
# 文件作者 : XXX
# 电子邮箱 : XXX
# 修改日期 : 2021/9/26
#
# @ 本 Tcl 脚本用于 Modelsim 自动化仿真
#
######################################################################



############################  -参数定义-  #############################

# 待仿真的 tb 文件名称
set TBfileName      "testbench"

# 默认仿真时间        
set RunTimes        "50us"

# 文件列表路径     
set FileListPath    "./../FileList.lst"


######################################################################


# 退出仿真，清空命令行
    quit -sim
    .main clear

# 在根目录下建立库文件
    vlib ./lib/
    vlib ./lib/work

# 库文件地址映射
    vmap    work   ./lib/work


# 打开 List 文件
set fp [open $FileListPath r]
set FileStr ""
while {[gets $fp EachLine]!=-1} {
    if {$EachLine ne "0"} {
        append FileStr "\n" $EachLine
    }
}
close $fp
puts $FileStr

# 编译 Verilog 文件
    vlog -work      work        $FileStr

# 启动仿真器
    vsim    -voptargs=+acc  work.$TBfileName

# 添加 testbench 文件内的信号
    add wave    -divider {$TBfileName}
    add wave    $TBfileName/*
	

# 运行
    run $RunTimes
