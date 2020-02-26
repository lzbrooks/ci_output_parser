from ci_output_parser.log_file_parsers.regex_log_file_parser import RegexLogFileParser


class AndroidLogFileParser(RegexLogFileParser):
    def __init__(self, log_file_path=None, parser_name="Android API Target Lint", output_file_name=None,
                 file_parser_parameters=None):
        log_line_parser_parameters = dict(start_regex=None,
                                          stop_regex=None,
                                          parse_regex=r'^(?!Download)')
        lint_error_parser_parameters = dict(start_regex=None,
                                            stop_regex=r'> Lint found errors in the project; aborting build\.',
                                            parse_regex=r'.*')
        super().__init__(log_file_path=log_file_path, parser_name=parser_name, output_file_name=output_file_name,
                         file_parser_parameters=file_parser_parameters,
                         log_line_parser_parameters=log_line_parser_parameters,
                         lint_error_parser_parameters=lint_error_parser_parameters)

    def clean_lint_error_lines(self):
        if self.lint_lines \
                and ("Ran lint on variant release: 0 issues found\n" not in self.lint_lines) \
                and ("Ran lint on variant debug: 0 issues found\n" not in self.lint_lines):
            return
        self.lint_errors = []


class AndroidAppLogFileParser(AndroidLogFileParser):
    def __init__(self, log_file_path=None, api_version="Target"):
        parser_name = "Android API " + api_version + " App Lint"
        file_parser_parameters = dict(start_regex=r'^:app:lint|> Task :app:lint',
                                      stop_regex=r'^Wrote HTML report to|No issues found',
                                      parse_regex=r'.*')
        super().__init__(log_file_path=log_file_path, parser_name=parser_name,
                         file_parser_parameters=file_parser_parameters)


class AndroidModelsLogFileParser(AndroidLogFileParser):
    def __init__(self, log_file_path=None, api_version="Target"):
        parser_name = "Android API " + api_version + " Models Lint"
        file_parser_parameters = dict(start_regex=r'^:models:lint|> Task :models:lint',
                                      stop_regex=r'^Wrote HTML report to|BUILD SUCCESSFUL',
                                      parse_regex=r'.*')
        super().__init__(log_file_path=log_file_path, parser_name=parser_name,
                         file_parser_parameters=file_parser_parameters)


class AndroidBuildLogFileParser(RegexLogFileParser):
    def __init__(self, log_file_path=None, api_version="Target"):
        parser_name = "Android API " + api_version + " Build Lint"
        file_parser_parameters = dict(start_regex=r'^> Task .* FAILED\n$',
                                      stop_regex=None,
                                      parse_regex=r'.*')
        super().__init__(log_file_path=log_file_path, parser_name=parser_name,
                         file_parser_parameters=file_parser_parameters)


class AndroidKotlinLogFileParser(RegexLogFileParser):
    def __init__(self, log_file_path=None, api_version="Target"):
        parser_name = "Android API " + api_version + " Kotlin Lint"
        file_parser_parameters = dict(start_regex=None,
                                      stop_regex=None,
                                      parse_regex=r'^w: ')
        super().__init__(log_file_path=log_file_path, parser_name=parser_name,
                         file_parser_parameters=file_parser_parameters)


class AndroidJavacLogFileParser(RegexLogFileParser):
    def __init__(self, log_file_path=None, parser_name="Android API Target Javac Lint", file_parser_parameters=None):
        log_line_parser_parameters = dict(start_regex=None,
                                          stop_regex=None,
                                          parse_regex=r'^[0-9]+ warnings$')
        super().__init__(log_file_path=log_file_path, parser_name=parser_name,
                         file_parser_parameters=file_parser_parameters,
                         log_line_parser_parameters=log_line_parser_parameters)

    def clean_lint_error_lines(self):
        if self.lint_lines:
            self.lint_errors = self.log_lines
        else:
            self.lint_errors = []


class AndroidDebugJavacLogFileParser(RegexLogFileParser):
    def __init__(self, log_file_path=None, api_version="Target"):
        parser_name = "Android API " + api_version + " Debug Javac Lint"
        file_parser_parameters = dict(start_regex=r'^> Task :app:compileDebugJavaWithJavac',
                                      stop_regex=r'^[0-9]+ warnings$',
                                      parse_regex=r'.*')
        super().__init__(log_file_path=log_file_path, parser_name=parser_name,
                         file_parser_parameters=file_parser_parameters)


class AndroidReleaseJavacLogFileParser(RegexLogFileParser):
    def __init__(self, log_file_path=None, api_version="Target"):
        parser_name = "Android API " + api_version + " Release Javac Lint"
        file_parser_parameters = dict(start_regex=r'^> Task :app:compileReleaseJavaWithJavac',
                                      stop_regex=r'^[0-9]+ warnings$',
                                      parse_regex=r'.*')
        super().__init__(log_file_path=log_file_path, parser_name=parser_name,
                         file_parser_parameters=file_parser_parameters)
