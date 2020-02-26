var releaseRules = [{
    "type": "Add",
    "release": "minor"
}, {
    "type": "Start",
    "release": "minor"
}, {
    "type": "Drop",
    "release": "major"
}, {
    "type": "Stop",
    "release": "major"
}, {
    "type": "Fix",
    "release": "patch"
}, {
    "type": "Bump",
    "release": "patch"
}, {
    "type": "Make",
    "release": "patch"
}, {
    "type": "Optimize",
    "release": "patch"
}, {
    "type": "Document",
    "release": "patch"
}, {
    "type": "Refactor",
    "release": "patch"
}, {
    "type": "Reformat",
    "release": "patch"
}, {
    "type": "Rearrange",
    "release": "patch"
}, {
    "type": "Redraw",
    "release": "patch"
}, {
    "type": "Reword",
    "release": "patch"
}];

var parserOpts = {
    headerPattern: /^(\w*)[ ]?(.*)$/,
    headerCorrespondence: [
        'type',
        'subject'
    ],
};

var LABELS = {
    NewFeatures: {
        title: 'New features'
    },
    BreakingChanges: {
        title: 'Breaking changes'
    },
    Fixes: {
        title: 'Fixes'
    },
    Maintenance: {
        title: 'Maintenance'
    },
    Cleanup: {
        title: 'Cleanup'
    }
};

var sort = Object.keys(LABELS);

var writerOpts = {
    transform: function(commit) {
        if (commit.type === 'Add' ||
            commit.type === 'Start') {
            commit.type = 'New features';
        } else if (commit.type === 'Drop' ||
            commit.type === 'Stop') {
            commit.type = 'Breaking changes';
        } else if (commit.type === 'Fix') {
            commit.type = 'Fixes';
        } else if (commit.type === 'Bump' ||
            commit.type === 'Make' ||
            commit.type === 'Optimize' ||
            commit.type === 'Document') {
            commit.type = 'Maintenance';
        } else if (commit.type === 'Refactor' ||
            commit.type === 'Reformat' ||
            commit.type === 'Rearrange' ||
            commit.type === 'Redraw' ||
            commit.type === 'Reword') {
            commit.type = 'Cleanup';
        } else {
            return;
        }
        return commit;
    },
    groupBy: 'type',
    commitGroupsSort: function(commitGroup, otherCommitGroup) {
        return sort.indexOf(commitGroup.title) > sort.indexOf(otherCommitGroup.title);
    },
    commitsSort: ['header']
};

var types = [{
    "type": "Add",
    "section": "New features"
}, {
    "type": "Start",
    "section": "New features"
}, {
    "type": "Drop",
    "section": "Breaking changes"
}, {
    "type": "Stop",
    "section": "Breaking changes"
}, {
    "type": "Fix",
    "section": "Fixes"
}, {
    "type": "Bump",
    "section": "Maintenance"
}, {
    "type": "Make",
    "section": "Maintenance"
}, {
    "type": "Optimize",
    "section": "Maintenance"
}, {
    "type": "Document",
    "section": "Maintenance"
}, {
    "type": "Refactor",
    "section": "Cleanup"
}, {
    "type": "Reformat",
    "section": "Cleanup"
}, {
    "type": "Rearrange",
    "section": "Cleanup"
}, {
    "type": "Redraw",
    "section": "Cleanup"
}, {
    "type": "Reword",
    "section": "Cleanup"
}];

module.exports = {
    branch: "master",
    plugins: [
        ["@semantic-release/commit-analyzer", {
            config: "@commitlint/config-conventional",
            releaseRules: releaseRules,
            parserOpts: parserOpts
        }],
        ["@semantic-release/changelog", {
            preset: "conventionalcommits",
            types: types
        }],
        ["@semantic-release/release-notes-generator", {
            parserOpts: parserOpts,
            writerOpts: writerOpts
        }],
        ["@semantic-release/github", {
            assets: [{
                path: 'ci_output_parser-*-py3-none-any.whl',
                name: 'ci_output_parser-${nextRelease.gitTag}-py3-none-any.whl',
                label: 'CIOutputParser (${nextRelease.gitTag}) wheel'
            }, {
                path: 'ci_output_parser-*.tar.gz',
                name: 'ci_output_parser-${nextRelease.gitTag}.tar.gz',
                label: 'CIOutputParser (${nextRelease.gitTag}) tar'
            }, {
                path: 'CHANGELOG.md',
                name: 'CIOutputParser-Changelog-${nextRelease.gitTag}.md',
                label: 'Changelog (${nextRelease.gitTag})'
            }, {
                path: 'docs.zip',
                name: 'CIOutputParser-Docs-${nextRelease.gitTag}.zip',
                label: 'Docs (${nextRelease.gitTag})'
            }],
            successComment: "This ${issue.pull_request ? 'pull request' : 'issue'} is included in version ${nextRelease.version}",
            failtTitle: "Automated release is failing",
            labels: ["bug"],
            assignees: ["brookslz"],
            releasedLabels: false
        }]
    ]
};
