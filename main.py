import os
import random
import subprocess
from datetime import datetime, timedelta

def get_positive_int(prompt, default=20):
    while True:
        try:
            user_input = input(f"{prompt} (default {default}): ")
            if not user_input.strip():
                return default
            value = int(user_input)
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_repo_path(prompt, default="."):
    while True:
        user_input = input(f"{prompt} (default current directory): ")
        if not user_input.strip():
            return default
        if os.path.isdir(user_input):
            return user_input
        else:
            print("Directory does not exist. Please enter a valid path.")

def get_filename(prompt, default="data.txt"):
    user_input = input(f"{prompt} (default {default}): ")
    if not user_input.strip():
        return default
    return user_input

def random_date_in_last_year():
    today = datetime.now()
    start_date = today - timedelta(days=365)
    random_days = random.randint(0, 364)
    random_seconds = random.randint(0, 23*3600 + 3599)
    commit_date = start_date + timedelta(days=random_days, seconds=random_seconds)
    return commit_date

def make_commit(date, repo_path, filename, message="graph-greener!"):
    filepath = os.path.join(repo_path, filename)
    with open(filepath, "a") as f:
        f.write(f"Commit at {date.isoformat()}\n")
    subprocess.run(["git", "add", filename], cwd=repo_path)
    env = os.environ.copy()
    date_str = date.strftime("%Y-%m-%dT%H:%M:%S")
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    subprocess.run(["git", "commit", "-m", message], cwd=repo_path, env=env)

def main():
    print("="*60)
    print("🌱 Welcome to graph-greener - GitHub Contribution Graph Commit Generator 🌱")
    print("="*60)
    print("This tool will help you fill your GitHub contribution graph with custom commits.\n")

    num_commits = get_positive_int("How many commits do you want to make", 20)
    repo_path = get_repo_path("Enter the path to your local git repository", ".")
    filename = get_filename("Enter the filename to modify for commits", "data.txt")

    print(f"\nMaking {num_commits} commits in repo: {repo_path}\nModifying file: {filename}\n")

    for i in range(num_commits):
        commit_date = random_date_in_last_year()
        print(f"[{i+1}/{num_commits}] Committing at {commit_date.strftime('%Y-%m-%d %H:%M:%S')}")
        make_commit(commit_date, repo_path, filename)

    print("\nPushing commits to your remote repository...")
    subprocess.run(["git", "push"], cwd=repo_path)
    print("✅ All done! Check your GitHub contribution graph in a few minutes.\n")
    print("Tip: Use a dedicated repository for best results. Happy coding!")

if __name__ == "__main__":
    main()Commit at 2025-12-06T11:30:35.000847
Commit at 2025-08-16T17:24:02.066682
Commit at 2025-12-07T22:04:55.113311
Commit at 2025-12-23T22:52:26.160099
Commit at 2026-01-13T12:44:04.203484
Commit at 2025-12-31T18:02:53.247428
Commit at 2025-08-27T15:39:49.290792
Commit at 2026-02-17T13:47:00.335241
Commit at 2025-09-28T16:34:44.379996
Commit at 2026-04-23T14:48:17.427845
Commit at 2025-12-01T10:02:38.471170
Commit at 2025-12-16T06:37:47.515060
Commit at 2025-08-13T16:04:11.557758
Commit at 2025-09-13T11:42:39.600297
Commit at 2025-11-08T19:58:41.651522
Commit at 2025-12-26T12:21:43.707120
Commit at 2025-07-29T08:42:58.750616
Commit at 2025-05-24T02:42:48.793679
Commit at 2025-06-04T04:50:29.837613
Commit at 2025-09-06T01:36:42.884041
Commit at 2026-02-15T01:08:52.927869
Commit at 2026-02-16T08:35:18.970642
Commit at 2026-03-02T22:22:14.015365
Commit at 2026-04-19T08:40:07.059275
Commit at 2025-08-11T16:32:30.102278
Commit at 2025-07-15T15:53:20.148624
Commit at 2025-10-18T11:06:01.195149
Commit at 2026-03-29T07:07:18.238089
Commit at 2025-06-24T22:45:35.281070
Commit at 2025-09-05T12:01:38.324012
Commit at 2026-04-17T06:51:05.367518
Commit at 2026-03-14T23:10:42.413926
Commit at 2026-03-30T10:45:19.457650
Commit at 2026-03-28T23:42:48.501380
Commit at 2025-07-11T19:12:05.546226
Commit at 2025-07-20T19:11:01.588823
Commit at 2025-07-22T14:05:01.631661
Commit at 2025-09-07T13:49:04.678976
Commit at 2026-03-20T22:54:32.723445
Commit at 2026-04-14T06:03:27.768125
Commit at 2025-10-08T11:34:07.811058
Commit at 2026-02-15T12:13:51.851708
Commit at 2026-04-23T01:47:30.896011
Commit at 2025-06-24T00:27:50.938698
Commit at 2025-12-04T20:15:32.980831
Commit at 2025-08-21T21:58:23.023154
Commit at 2026-03-29T01:34:21.066262
Commit at 2025-12-05T00:56:21.111169
Commit at 2026-01-08T16:48:41.156669
Commit at 2025-10-11T01:23:12.200943
Commit at 2025-10-08T21:54:12.243935
Commit at 2025-08-15T07:16:41.287355
Commit at 2025-09-17T10:20:29.335247
Commit at 2025-11-24T13:01:47.381339
Commit at 2025-11-17T08:03:12.424623
Commit at 2025-06-10T00:23:06.466746
Commit at 2026-02-15T13:32:25.510500
Commit at 2025-10-02T05:09:09.553713
Commit at 2025-09-18T21:55:20.597288
Commit at 2025-11-05T10:58:20.642074
Commit at 2025-09-29T07:46:12.689418
Commit at 2025-11-07T05:02:26.732478
Commit at 2025-11-12T22:09:24.777004
Commit at 2026-01-20T18:47:36.820725
Commit at 2025-05-28T17:26:49.864661
Commit at 2025-08-30T14:05:21.907377
Commit at 2026-04-25T03:04:44.950263
Commit at 2026-01-31T07:14:22.993023
Commit at 2025-07-02T06:24:34.039003
Commit at 2026-03-17T02:51:29.085962
Commit at 2025-05-29T14:01:37.133034
Commit at 2025-08-27T05:53:29.182083
Commit at 2025-11-20T02:21:30.228330
Commit at 2025-10-01T08:55:38.270514
Commit at 2025-07-12T07:19:13.315565
Commit at 2025-07-29T23:49:22.361582
Commit at 2025-12-07T20:07:40.407510
Commit at 2025-08-22T11:36:31.449892
Commit at 2025-09-17T21:56:51.495911
Commit at 2025-07-20T01:08:00.537407
Commit at 2026-04-17T13:29:04.580963
Commit at 2025-11-24T21:12:32.626863
Commit at 2025-08-04T20:02:25.671362
Commit at 2026-01-11T08:41:50.717711
Commit at 2025-09-19T15:45:27.761017
Commit at 2025-10-05T10:31:58.823682
Commit at 2025-05-26T03:28:55.868886
Commit at 2026-01-17T08:03:37.912940
Commit at 2025-06-12T08:15:08.956127
Commit at 2025-10-19T14:11:14.001045
Commit at 2026-04-23T05:02:15.045754
Commit at 2025-07-25T18:02:47.089050
Commit at 2025-07-25T21:22:01.135539
Commit at 2025-11-04T14:57:38.183701
Commit at 2025-06-10T21:32:48.231903
Commit at 2026-05-18T10:46:46.276635
Commit at 2026-04-28T08:23:40.319706
Commit at 2026-02-13T13:58:42.364466
Commit at 2026-02-09T23:18:33.409885
Commit at 2025-06-30T15:41:32.452256
Commit at 2025-11-16T06:11:57.495963
Commit at 2025-06-09T01:57:16.537842
Commit at 2026-05-12T07:29:16.581070
Commit at 2025-12-13T07:24:31.623611
Commit at 2026-03-13T22:42:43.670298
Commit at 2025-10-19T03:34:08.719263
Commit at 2025-09-17T21:34:29.763916
Commit at 2025-09-11T21:34:42.809311
Commit at 2025-07-30T01:36:16.856776
Commit at 2025-05-24T20:28:19.903115
Commit at 2025-10-13T17:47:21.945759
Commit at 2026-04-11T16:32:23.989173
Commit at 2026-03-13T18:14:52.034065
Commit at 2025-07-06T08:53:33.076040
Commit at 2025-06-10T15:11:15.119351
Commit at 2025-09-27T04:22:18.165862
Commit at 2026-03-20T04:40:13.215810
Commit at 2025-08-24T15:58:58.259868
Commit at 2026-02-20T19:29:46.303667
Commit at 2025-09-03T02:56:26.350690
Commit at 2025-10-11T12:54:13.397115
Commit at 2025-10-12T04:31:42.442837
Commit at 2026-03-25T13:54:30.486946
Commit at 2026-01-12T21:56:03.530411
Commit at 2025-08-05T20:45:41.571385
Commit at 2025-07-23T15:16:02.613906
Commit at 2026-01-12T12:04:52.658356
Commit at 2025-06-02T06:01:54.707343
Commit at 2025-05-30T19:18:57.753524
Commit at 2025-07-02T04:11:35.798041
Commit at 2025-08-23T19:53:23.843604
Commit at 2026-02-21T11:58:38.890878
Commit at 2026-01-15T17:04:28.936146
Commit at 2026-02-02T02:18:46.979381
Commit at 2026-05-13T05:15:46.020241
Commit at 2025-09-08T01:43:20.062852
Commit at 2025-12-04T02:11:30.105312
Commit at 2026-05-20T04:23:09.147229
Commit at 2026-01-07T19:50:57.189737
Commit at 2026-01-15T03:43:08.236192
Commit at 2025-07-14T13:37:11.280868
Commit at 2025-11-22T01:32:17.323562
Commit at 2026-04-09T10:27:58.370508
Commit at 2025-11-29T11:51:15.416774
Commit at 2025-05-31T14:43:33.460472
Commit at 2026-04-19T08:48:10.501871
Commit at 2025-08-28T01:48:43.544154
Commit at 2025-09-21T17:30:07.586722
Commit at 2026-04-13T21:04:29.629871
Commit at 2025-06-12T04:55:59.673092
Commit at 2025-09-08T08:02:43.720061
Commit at 2025-07-12T15:54:59.764625
Commit at 2026-01-17T09:42:07.806530
Commit at 2026-01-29T19:30:51.852172
Commit at 2026-05-18T02:55:26.898974
Commit at 2025-10-27T11:05:35.943894
Commit at 2025-08-25T07:25:33.984958
Commit at 2025-06-04T14:47:29.027925
Commit at 2026-05-21T05:33:57.069995
Commit at 2025-08-16T17:05:38.113463
Commit at 2026-01-12T02:02:54.154151
Commit at 2025-11-22T08:52:19.196929
Commit at 2026-03-31T03:44:12.241016
Commit at 2026-03-15T23:13:34.285046
Commit at 2026-03-02T03:18:31.328547
Commit at 2025-10-02T16:12:10.370913
Commit at 2026-03-17T17:17:38.415520
Commit at 2025-07-09T14:45:46.458234
Commit at 2026-04-27T09:58:26.501884
Commit at 2025-06-05T08:35:18.556598
Commit at 2026-03-26T08:31:46.598153
Commit at 2025-08-02T20:32:08.640305
