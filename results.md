# Lab DA-1 Results

## Objective

Implemented a Python Remote Procedure Call (RPC) framework that supports remote invocation of:

`float calculate_grade_average(StudentProfile profile)`

The `StudentProfile` object contains:

- `name` as `string`
- `id` as `int`
- `grades` as `list[int]`

## Files Added

- `rpc_marshalling_url/models.py`
- `rpc_marshalling_url/marshalling.py`
- `rpc_marshalling_url/server.py`
- `rpc_marshalling_url/client.py`
- `rpc_marshalling_url/demo.py`

## validate_types() Implementation

The server-side marshalling layer includes a `validate_types()` function in `rpc_marshalling_url/marshalling.py`.

It validates:

- Top-level RPC structure
- Required fields in `StudentProfile`
- Exact Python types for scalar fields
- Element types inside `grades`

If a client sends a string where an `int` is expected, the server raises a `TypeError` and returns the error in the RPC response.

Example invalid payload:

```json
{
  "method": "calculate_grade_average",
  "params": {
    "name": "Asha",
    "id": "21",
    "grades": [90, 80, 70]
  }
}
```

Expected server-side error:

```text
payload.params.id expected int, got str
```

## Sample Run

Command:

```powershell
python -m rpc_marshalling_url.demo
```

Observed output:

```text
Valid RPC result: 85.00
Invalid RPC response: payload.params.id expected int, got str
```

## Submission Note

This workspace is not currently a Git repository, so branch creation, commit, push, and PR creation could not be completed here. Once these files are copied into the actual GitHub repository, the expected submission flow is:

```powershell
git checkout -b rpc-marshalling-objects
git add .
git commit -m "Implement RPC marshalling for StudentProfile"
git push origin rpc-marshalling-objects
```

Then open a Pull Request to `main`, include `results.md`, and tag `@manoov`.
