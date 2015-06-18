{
  "targets": [
    {
      "target_name": "binding",
      "sources": [
        "src/bridge.cc"
      ],
      "conditions": [
        ["OS=='mac'",
          {
            "defines": [
              "__MACOSX_CORE__"
            ],
            "xcode_settings": {
              "GCC_ENABLE_CPP_EXCEPTIONS": "YES"
            },
            "link_settings": {
              "libraries": [
                "Phidget21.framework"
              ]
            },
            'include_dirs': [ '/Library/Frameworks/Phidget21.framework/Headers' ],
            'libraries': [ '-L/Library/Frameworks/Phidget21.framework' ]
          }
        ],
        ["OS=='win'",
          {
            "defines": [
              "__WINDOWS_MM__"
            ],
            "link_settings": {
              "libraries": [
                "phidget21.lib"
              ]
            }
          }
        ],
        ["OS=='linux'",
          {
            "defines": [
              "__LINUX__"
            ],
            "link_settings": {
              "libraries": [
                "/usr/lib/libphidget21.so"
              ]
            }
          }
        ]
      ]
    }
  ]
}
