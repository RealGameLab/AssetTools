# UnusedAssetsCollection

将cook中使用的和未使用的assets收集到两个collection上

## 参数
- --projectPath: 工程路径
- --cookLogPath：CookerOpenOrder.log 文件路径

## 用法
项目路径下新建批处理`UnusedAssetsCollection.bat`

```
..\Engine\Extras\UnusedAssetsCollection\UnusedAssetsCollection.bat --projectPath=%~dp0 --cookLogPath=%~dp0Build\Android_ETC2\FileOpenOrder\CookerOpenOrder.log
```

cook后运行`UnusedAssetsCollection.bat`，collection中会多出两个collection，分别是使用和未使用的assets
![result](https://raw.githubusercontent.com/RealGameLab/UnusedAssetsCollection/master/result.jpg)
![result2](https://raw.githubusercontent.com/RealGameLab/UnusedAssetsCollection/master/result2.jpg)