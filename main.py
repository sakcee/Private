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
Commit at 2025-09-27T17:57:40.681774
Commit at 2026-04-08T07:03:20.725703
Commit at 2025-09-08T12:02:03.768931
Commit at 2026-04-15T21:17:20.812257
Commit at 2025-06-08T16:44:30.855758
Commit at 2025-12-28T12:47:12.898694
Commit at 2026-02-24T16:41:04.943168
Commit at 2025-06-11T06:23:37.986313
Commit at 2026-02-19T20:35:59.028963
Commit at 2026-04-11T14:19:39.070491
Commit at 2025-06-18T06:26:00.110886
Commit at 2025-12-01T19:24:52.153401
Commit at 2025-09-25T12:10:12.194661
Commit at 2025-06-09T00:32:58.238367
Commit at 2026-05-10T00:47:37.282157
Commit at 2026-01-02T05:21:08.326294
Commit at 2026-04-03T14:48:48.368945
Commit at 2025-07-25T12:47:51.413169
Commit at 2026-05-09T16:34:46.457124
Commit at 2026-04-22T00:41:08.499948
Commit at 2025-12-27T06:08:43.542839
Commit at 2025-09-08T00:17:35.584387
Commit at 2025-05-23T07:02:30.625321
Commit at 2026-02-03T21:54:12.667480
Commit at 2025-06-09T11:32:21.709967
Commit at 2025-12-27T22:24:05.753985
Commit at 2026-01-07T03:46:06.797494
Commit at 2025-12-31T23:15:37.838233
Commit at 2025-06-21T03:27:49.880896
Commit at 2025-11-09T22:25:02.924680
Commit at 2025-06-23T07:22:30.969491
Commit at 2025-12-17T08:03:08.012592
Commit at 2026-02-05T01:58:28.053154
Commit at 2025-09-11T14:44:20.094421
Commit at 2025-08-17T09:38:33.134945
Commit at 2025-11-17T04:05:00.177159
Commit at 2026-01-05T03:17:47.220227
Commit at 2026-03-04T17:21:17.266551
Commit at 2025-06-09T14:10:22.309077
Commit at 2025-06-13T10:51:22.351730
Commit at 2025-11-11T15:06:30.395278
Commit at 2026-02-10T20:02:27.437883
Commit at 2026-03-21T09:37:27.480952
Commit at 2025-08-27T02:28:25.523995
Commit at 2026-01-14T06:38:56.564699
Commit at 2026-02-21T18:19:42.605474
Commit at 2026-04-12T22:51:34.645529
Commit at 2025-09-09T17:37:43.685791
Commit at 2025-10-12T13:58:15.728182
Commit at 2025-10-26T01:49:41.772048
Commit at 2026-04-26T14:55:37.814915
Commit at 2025-06-18T09:12:48.857396
Commit at 2025-10-02T07:22:53.897159
Commit at 2025-10-09T22:34:32.941872
Commit at 2026-02-06T10:56:14.984002
Commit at 2025-12-07T15:38:16.028442
Commit at 2025-09-16T01:12:27.070406
Commit at 2026-05-20T21:02:38.110783
Commit at 2025-10-22T12:25:34.150664
Commit at 2025-07-01T05:50:35.192443
Commit at 2025-06-15T20:46:03.233200
Commit at 2025-09-29T08:50:53.274542
Commit at 2026-01-10T14:50:14.317295
Commit at 2025-12-18T18:43:07.358809
Commit at 2025-12-02T03:03:44.400204
Commit at 2026-01-25T09:55:07.440878
Commit at 2026-02-05T07:59:32.484881
Commit at 2026-04-09T10:13:01.527335
Commit at 2025-09-05T19:07:44.570016
Commit at 2025-07-24T15:46:53.610495
Commit at 2025-11-14T21:06:53.651455
Commit at 2025-09-26T09:35:52.692896
Commit at 2025-12-27T08:35:28.733732
Commit at 2025-07-26T15:06:43.776807
Commit at 2026-03-29T20:48:50.820046
Commit at 2025-09-15T10:19:38.863184
Commit at 2025-10-03T10:53:04.907570
Commit at 2026-02-22T23:30:31.951633
Commit at 2026-04-20T15:57:07.997374
Commit at 2026-05-21T06:14:36.040449
Commit at 2025-06-17T13:48:02.080985
Commit at 2026-02-02T11:21:00.122619
Commit at 2026-04-16T09:23:11.162305
Commit at 2025-06-12T11:55:04.201719
Commit at 2026-04-27T13:15:06.243066
Commit at 2025-08-17T05:31:08.301971
Commit at 2025-07-23T10:52:03.348454
Commit at 2025-08-06T17:13:33.391227
Commit at 2025-05-31T05:40:50.433969
Commit at 2025-05-28T04:44:53.477714
Commit at 2026-02-06T06:55:22.519676
Commit at 2026-02-20T10:07:49.563790
Commit at 2026-03-22T01:05:12.606142
Commit at 2025-09-29T15:26:53.646452
Commit at 2025-07-29T18:57:32.686365
Commit at 2026-01-26T00:42:12.726629
Commit at 2025-12-08T23:27:52.768472
Commit at 2025-07-10T05:34:25.810564
Commit at 2025-09-08T09:10:29.851936
Commit at 2026-04-17T09:32:19.894235
Commit at 2025-08-28T09:21:44.936270
Commit at 2026-02-21T05:24:20.979166
Commit at 2026-05-18T10:09:07.021260
Commit at 2026-04-09T01:19:13.064618
Commit at 2026-04-16T16:52:49.106444
Commit at 2025-07-31T19:04:23.145992
Commit at 2025-10-21T18:18:29.186463
Commit at 2026-04-17T18:22:01.227316
Commit at 2026-02-21T04:38:40.268274
Commit at 2026-03-09T17:50:02.310945
Commit at 2026-03-03T02:53:55.351941
Commit at 2025-11-15T05:38:55.393783
Commit at 2025-07-27T09:53:19.435227
Commit at 2026-04-07T03:51:54.476867
Commit at 2026-01-09T11:57:39.519923
Commit at 2026-01-07T02:44:12.563697
Commit at 2025-11-19T10:23:05.606348
Commit at 2025-12-04T08:35:14.646336
Commit at 2025-06-30T21:58:39.686301
Commit at 2026-01-18T01:21:59.725215
Commit at 2025-10-05T11:26:01.767797
Commit at 2025-11-14T19:31:14.811718
Commit at 2026-01-03T17:29:08.854546
Commit at 2025-09-23T01:33:58.895289
Commit at 2025-08-25T15:58:45.935663
Commit at 2026-03-09T00:01:25.976822
Commit at 2025-09-15T10:24:39.017099
Commit at 2025-11-24T11:13:14.060021
Commit at 2026-04-09T02:57:16.102072
Commit at 2025-09-21T20:40:27.143405
Commit at 2025-11-26T08:58:33.183389
Commit at 2025-12-02T18:55:15.223225
Commit at 2025-09-07T06:10:48.262581
Commit at 2026-04-04T06:05:11.304422
Commit at 2026-04-29T21:48:37.347099
Commit at 2025-05-22T19:17:19.388819
Commit at 2025-09-14T06:01:09.428449
Commit at 2025-11-11T22:45:05.468525
Commit at 2025-10-11T23:05:58.509650
Commit at 2026-03-19T21:27:15.549260
Commit at 2026-05-05T19:30:06.592278
Commit at 2025-06-15T02:35:03.633987
Commit at 2025-07-14T08:00:16.674352
Commit at 2025-08-23T18:44:35.713582
Commit at 2025-12-29T11:17:17.754790
Commit at 2026-05-17T12:27:36.796791
Commit at 2025-07-25T06:52:50.840085
Commit at 2025-05-30T21:15:56.879936
Commit at 2026-01-16T03:48:22.920139
Commit at 2026-04-25T12:13:03.960069
Commit at 2026-02-06T10:05:26.001095
Commit at 2026-04-12T18:43:40.043955
Commit at 2026-04-01T01:12:13.085122
Commit at 2026-03-10T07:46:17.126093
Commit at 2025-08-08T05:35:48.165274
Commit at 2025-11-07T10:10:14.206361
Commit at 2025-10-12T00:10:30.246170
Commit at 2025-06-04T07:45:39.287003
Commit at 2026-05-01T22:01:22.330174
Commit at 2025-08-03T06:08:44.371174
Commit at 2025-10-24T05:03:22.411998
Commit at 2025-06-26T02:31:43.453099
Commit at 2025-07-23T18:31:55.493712
Commit at 2026-02-26T23:31:25.534437
Commit at 2025-06-12T01:16:13.574751
Commit at 2026-02-25T13:20:08.615958
Commit at 2026-04-23T13:51:24.656517
Commit at 2025-06-18T06:57:04.696243
Commit at 2025-06-10T08:23:15.736886
Commit at 2025-05-31T12:09:27.777275
Commit at 2025-07-12T04:13:51.816892
Commit at 2026-05-09T06:58:42.880253
Commit at 2025-10-20T00:30:14.925925
Commit at 2026-03-13T06:44:37.965569
Commit at 2026-03-05T04:32:38.006451
Commit at 2025-11-09T08:08:02.047067
Commit at 2025-09-16T10:00:16.088095
Commit at 2026-03-16T03:52:27.128658
Commit at 2025-10-22T09:43:09.169038
Commit at 2025-12-19T10:15:33.209678
Commit at 2025-09-30T20:26:58.251199
Commit at 2025-05-29T15:24:09.292464
Commit at 2026-01-24T16:26:13.332920
Commit at 2026-03-05T02:29:05.377117
Commit at 2026-05-13T19:56:54.416656
Commit at 2025-05-22T20:51:11.457352
