using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;

public static class ScriptBuild 
{
    public static void Build()
    {
        BuildPlayerOptions buildPlayerOptions = new BuildPlayerOptions();
        buildPlayerOptions.scenes = new[] { "Assets/scene.unity" };
        buildPlayerOptions.locationPathName = "scriptBuilds";
        buildPlayerOptions.target = BuildTarget.StandaloneOSX;

        // use these options for the first build
        buildPlayerOptions.options = BuildOptions.Development;

        // use these options for building scripts
        // buildPlayerOptions.options = BuildOptions.BuildScriptsOnly | BuildOptions.Development;

        BuildPipeline.BuildPlayer(buildPlayerOptions);
    }
}
