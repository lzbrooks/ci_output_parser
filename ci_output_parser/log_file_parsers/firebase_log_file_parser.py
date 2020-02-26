import re

from ci_output_parser.log_file_parsers.regex_log_file_parser import RegexLogFileParser


class FirebaseLogFileParser(RegexLogFileParser):
    def __init__(self, log_file_path=None, parser_name="Firebase Lint", output_file_name=None,
                 file_parser_parameters=None, log_line_parser_parameters=None):
        super().__init__(log_file_path=log_file_path, parser_name=parser_name, output_file_name=output_file_name,
                         file_parser_parameters=file_parser_parameters,
                         log_line_parser_parameters=log_line_parser_parameters)

    def format_lint_errors(self):
        if self.lint_errors:
            print("Formatting %s log lint lines" % len(self.lint_errors))
            for error_line in self.lint_errors:
                error_line = error_line + "\n"
                self.formatted_lines.append(error_line)


class FirebaseBucketLogFileParser(FirebaseLogFileParser):
    def __init__(self, log_file_path=None, parser_name="Firebase Bucket Path"):
        log_line_parser_parameters = dict(start_regex=None,
                                          stop_regex=None,
                                          parse_regex=r'gs:\/\/.*')
        super().__init__(log_file_path=log_file_path, parser_name=parser_name,
                         log_line_parser_parameters=log_line_parser_parameters)

    def clean_lint_error_lines(self):
        if any("Failed" in line for line in self.log_lines):
            self.lint_errors = [x[33:-3] for x in self.lint_errors]
        else:
            self.lint_errors = []


class FirebaseDeviceLogFileParser(FirebaseLogFileParser):
    def __init__(self, log_file_path=None, parser_name="Firebase Device Folders"):
        file_parser_parameters = dict(start_regex=None,
                                      stop_regex=None,
                                      parse_regex=r'Failed')
        super().__init__(log_file_path=log_file_path, parser_name=parser_name,
                         file_parser_parameters=file_parser_parameters)

    def clean_lint_error_lines(self):
        device_folders = []
        for error_line in self.lint_errors:
            error_split_list = re.split(r' +', error_line)
            device_folders.append(error_split_list[3])
        self.lint_errors = device_folders


class FirebaseTestLogFileParser(RegexLogFileParser):
    def __init__(self, log_file_path=None, device_name="Device"):
        parser_name = "Firebase " + device_name + " Tests"
        file_parser_parameters = dict(start_regex=r'^There were|There was',
                                      stop_regex=r'^INSTRUMENTATION_CODE',
                                      parse_regex=r'.*')
        log_line_parser_parameters = dict(start_regex=None,
                                          stop_regex=None,
                                          parse_regex=r'failure')
        super().__init__(log_file_path=log_file_path, parser_name=parser_name,
                         file_parser_parameters=file_parser_parameters,
                         log_line_parser_parameters=log_line_parser_parameters)

    def clean_lint_error_lines(self):
        source_error_lines = []
        if self.lint_lines:
            for error_line in self.log_lines:
                if error_line.startswith("	at ") and (
                        error_line.startswith("	at org.junit.runner") or
                        error_line.startswith("	at org.junit.internal") or
                        error_line.startswith("	at androidx.test") or
                        error_line.startswith("	at android.app.Instrumentation") or
                        error_line.startswith("	at org.mockito.internal")):
                    continue
                else:
                    source_error_lines.append(error_line)
        self.lint_errors = source_error_lines


class FirebaseTestCrashLogFileParser(RegexLogFileParser):
    def __init__(self, log_file_path=None, device_name="Device"):
        parser_name = "Firebase " + device_name + " Tests"
        file_parser_parameters = dict(start_regex=None,
                                      stop_regex=r'^INSTRUMENTATION_CODE',
                                      parse_regex=r'.*')
        log_line_parser_parameters = dict(start_regex=None,
                                          stop_regex=None,
                                          parse_regex=r'shortMsg=Process crashed')
        super().__init__(log_file_path=log_file_path, parser_name=parser_name,
                         file_parser_parameters=file_parser_parameters,
                         log_line_parser_parameters=log_line_parser_parameters)

    def clean_lint_error_lines(self):
        if self.lint_lines:
            self.lint_errors = self.log_lines[-9:]
        else:
            self.lint_errors = []


class FirebaseTestTimeoutLogFileParser(RegexLogFileParser):
    def __init__(self, log_file_path=None, device_name="Device"):
        parser_name = "Firebase " + device_name + " Tests"
        log_line_parser_parameters = dict(start_regex=None,
                                          stop_regex=None,
                                          parse_regex=r'INSTRUMENTATION_CODE:')
        super().__init__(log_file_path=log_file_path, parser_name=parser_name,
                         log_line_parser_parameters=log_line_parser_parameters)

    def clean_lint_error_lines(self):
        timeout_lines = []
        if (not self.lint_lines) and self.log_lines:
            timeout_lines.append("Test Timed Out:\n")
            timeout_lines.append("\n")
            timeout_lines = timeout_lines + self.log_lines[-8:]
            self.lint_errors = timeout_lines
        else:
            self.lint_errors = []
