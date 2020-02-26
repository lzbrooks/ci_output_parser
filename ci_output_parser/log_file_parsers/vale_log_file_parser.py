from ci_output_parser.log_file_parsers.regex_log_file_parser import RegexLogFileParser


class ValeLogFileParser(RegexLogFileParser):
    def __init__(self, log_file_path=None, parser_name="Vale Lint", output_file_name=None,
                 file_parser_parameters=None):
        super().__init__(log_file_path=log_file_path, parser_name=parser_name, output_file_name=output_file_name,
                         file_parser_parameters=file_parser_parameters)

    def get_lint_lines(self):
        for line in self.log_lines:
            first_characters = line[0:6]
            if (first_characters != " ---> ") and \
                    ("0 errors, 0 warnings and 0 suggestions" not in line) and \
                    ("RUN vale" not in line):
                self.lint_lines.append(line)


class ValeDockerLogFileParser(ValeLogFileParser):
    def __init__(self, log_file_path=None):
        file_parser_parameters = dict(start_regex=r'vale.*docs',
                                      stop_regex=r'Removing intermediate container|non-zero code',
                                      parse_regex=r'.*')
        super().__init__(log_file_path=log_file_path, file_parser_parameters=file_parser_parameters)
