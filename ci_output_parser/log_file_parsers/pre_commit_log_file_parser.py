from ci_output_parser.log_file_parsers.regex_log_file_parser import RegexLogFileParser


class PreCommitLogFileParser(RegexLogFileParser):
    def __init__(self, log_file_path=None, parser_name="Pre-Commit Lint", output_file_name=None,
                 file_parser_parameters=None, log_line_parser_parameters=None):
        super().__init__(log_file_path=log_file_path, parser_name=parser_name, output_file_name=output_file_name,
                         file_parser_parameters=file_parser_parameters,
                         log_line_parser_parameters=log_line_parser_parameters)

    def get_lint_error_lines(self):
        for line in self.lint_lines:
            last_characters = line[-8:]
            if (last_characters != '.Passed\n') and (last_characters != 'Skipped\n'):
                self.lint_errors.append(line)

    def clean_lint_error_lines(self):
        if self.lint_errors:
            if self.lint_errors[0] == "CMakeLists.txt Diff\n":
                self.lint_errors = []


class PreCommitLogLogFileParser(PreCommitLogFileParser):
    def __init__(self, log_file_path=None):
        log_line_parser_parameters = dict(start_regex=r'Passed|Failed|Skipped$',
                                          stop_regex=r'^ ---> ',
                                          parse_regex=r'.*')
        super().__init__(log_file_path=log_file_path, log_line_parser_parameters=log_line_parser_parameters)


class PreCommitDockerLogFileParser(PreCommitLogFileParser):
    def __init__(self, log_file_path=None):
        file_parser_parameters = dict(start_regex=r'pre-commit run',
                                      stop_regex=r'Removing intermediate container|non-zero code',
                                      parse_regex=r'.*')
        log_line_parser_parameters = dict(start_regex=r'Passed|Failed|Skipped$',
                                          stop_regex=r'^ ---> ',
                                          parse_regex=r'.*')
        super().__init__(log_file_path=log_file_path, file_parser_parameters=file_parser_parameters,
                         log_line_parser_parameters=log_line_parser_parameters)
